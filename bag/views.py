from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product
from products.forms import ProductForm
from checkout.forms import QuoteForm


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def quote(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'bag/quote.html', context)


def add_to_quote(request, item_id):
    if request.method == 'POST':  # this means the form has data

        # get the session dictionary from the browser request or create one
        quote = request.session.get('quote', {})

        # look up the Product, search for it based on the post request "plan" value
        product = Product.objects.get(name=request.POST["plan"])
        # add the product id to the "quote" session dictionary
        # it will look like this:
        # {
        #     "quote": {
        #         "plan": 1
        #     }
        # }

        quote["plan"] = product.id
        # reassign the session quote dictionary back to the browser for when the page refreshes
        request.session["quote"] = quote
        # send a success message
        messages.success(request, ('Success! Your form was submitted'))
        return redirect('quote')
    else:
        messages.info(request, ('Error! Your form was not submitted'))
    return render(request, 'quote/quote.html')


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
