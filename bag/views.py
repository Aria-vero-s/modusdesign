from django.shortcuts import render, redirect
from products.models import Product
# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, **kwargs):
    # get the user profile

    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()

    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('products/quote.html'))



