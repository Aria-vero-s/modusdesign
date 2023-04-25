from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product, Service, Category
import logging

logger = logging.getLogger(__name__)


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def quote(request):
    products = Product.objects.all()
    services = Service.objects.all()
    logger.info('Services: {}'.format(services))
    logger.info('Products: {}'.format(products))
    context = {
        'products': products,
        'services': services,
    }
    return render(request, 'bag/quote.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def test(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/test.html')


def quoteslides(request):
    """
    A view that renders the quoteslides page,
    allowing users to add products to their shopping bag
    """
    bag = request.session.get('bag', {})
    products = []
    total = 0
    
    for product_id, quantity in bag.items():
        product = Product.objects.get(id=product_id)
        total += quantity * product.price
        products.append({
            'id': product_id,
            'name': product.name,
            'quantity': quantity,
            'price': product.price,
        })
    
    context = {
        'products': products,
        'total': total,
    }
    
    if request.method == 'POST':
        # Clear the bag and show a success message
        request.session['bag'] = {}
        messages.success(request, 'Your order has been placed!')
        return redirect(reverse('home'))
    
    return render(request, 'bag/quoteslides.html', context)