from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """A view that renders the bag contents page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    # product is assigned the product with the given item_id or raises a 404 error if the product does not exist.
    product = get_object_or_404(Product, pk=item_id)
    # quantity is assigned the integer value of the quantity field from the request's POST data.
    quantity = int(request.POST.get('quantity'))
    # redirect_url is assigned the value of the redirect_url field from the request's POST data.
    redirect_url = request.POST.get('redirect_url')
    # size is list of strings using the split() method
    size = request.POST.get('product_size').split(',')
    # If the product_size field is present in the request's POST data, size is assigned the value of the product_size field.
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # get the textarea input from the request POST data
    message = request.POST.get('message', '')
    # bag is assigned the current shopping bag from the user's session, or an empty dictionary if the bag does not yet exist.
    bag = request.session.get('bag', {})

    # If a size is specified for the product, the code block from line 9 to 23 updates the bag with the quantity of the product in that size.
    if size:
        # If the product with the given item_id is already in the bag, and the size is already in the bag for that product, the quantity for that size is incremented by the quantity value. A success message is displayed with the updated quantity.
        if item_id in list(bag.keys()):
            # If the product with the given item_id is already in the bag, but the size is not yet in the bag for that product, a new dictionary is created in the items_by_size key with the size as the key and the quantity as the value. A success message is displayed.
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            # If the product with the given item_id is not yet in the bag, a new dictionary is created in the bag dictionary with the item_id as the key and another dictionary as the value containing the items_by_size key with the size as the key and the quantity as the value. A success message is displayed.
            else:
                bag[item_id]['items_by_size'][size] = {'quantity': quantity, 'message': message}
                messages.success(request, f'Added {size.upper()} {product.name} to your bag')
        # If no size is specified for the product, the code block from line 24 to 29 updates the bag with the quantity of the product in any size.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added {size.upper()} {product.name} to your bag')
    else:
        # If the product with the given item_id is already in the bag, the quantity for that product is incremented by the quantity value. A success message is displayed with the updated quantity.
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        # If the product with the given item_id is not yet in the bag, a new key is created in the bag dictionary with the item_id as the key and the quantity as the value. A success message is displayed.
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
    
    # add the textarea input to the bag as a new key-value pair
    if message:
        bag[item_id] = {'items_by_size': {size: quantity}, 'message': message}
    
    # The bag dictionary is saved to the user's session.
    request.session['bag'] = bag

    # The function redirects the user to the redirect_url.
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

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
            messages.success(request, f'Removed {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)