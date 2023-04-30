from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from products.models import Product, Service, Category

# bag_contents takes in a request object as input
# and returns a dictionary called context

def bag_contents(request):

    bag_items = [] # an empty list to store the items in the shopping bag
    total = 0 # a variable to store the total price of all items in the bag
    product_count = 0 # a variable to store the total quantity of items in the bag
    bag = request.session.get('bag', {}) # retrieve the 'bag' dictionary from the session object, or an empty dictionary if it doesn't exist

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            service_price = 0
            services = get_list_or_404(Service)

            total += item_data * product.price + service_price
            product_count += item_data

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            services = get_list_or_404(Service)
            service_price = 0
            for service in services:
                if service.name == 'logo' and logo == 'true':
                    service_price += service.price * service.quantity

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data['quantity'],
                'product': product,
                'size': item_data['size'],
            })

            total += item_data['quantity'] * product.price + service_price
            product_count += item_data['quantity']

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # Add the selected products and services to the bag dictionary
    selected_services = request.POST.getlist('selected_services')
    selected_products = request.POST.getlist('selected_products')
    for service_id in selected_services:
        if service_id:
            service = get_object_or_404(Service, pk=service_id)
            bag_item_id = f's{service_id}'
            if bag_item_id in bag:
                bag[bag_item_id] += 1
            else:
                bag[bag_item_id] = 1
    for product_id in selected_products:
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            bag_item_id = f'p{product_id}'
            if bag_item_id in bag:
                bag[bag_item_id] += 1
            else:
                bag[bag_item_id] = 1

    # Save the modified bag dictionary to the session
    request.session['bag'] = bag

    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context