from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product, Service, Category
from django.urls import reverse


def view_bag(request):

    return render(request, 'bag/bag.html')


def quote(request):

    return render(request, 'bag/quote.html')


def test(request):
    
    return render(request, 'bag/test.html')


def quoteslides(request):
    products = Product.objects.all()
    services = Service.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'services': services,
        'categories': categories,
    }

    return render(request, 'bag/quoteslides.html', context)


def add_to_bag(request):
    # get the bag object from the request.session dictionary
    bag = request.session.get('bag', {})
    # get the list of products and services from the POST data
    products = request.POST.getlist('products')
    services = request.POST.getlist('services')
    # loop through each product_id in the products list (same for services),
    # and add it to the bag dictionary with a value of 1
    # (or increment the existing value by 1, if the product_id is already in the bag)
    for product_id in products:
        bag[product_id] = bag.get(product_id, 0) + 1

    for service_id in services:
        bag[service_id] = bag.get(service_id, 0) + 1
    # save the bag dictionary back to the request.session
    request.session['bag'] = bag
    # redirect the user to the page URL
    return redirect(reverse('bag:quoteslides'))


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