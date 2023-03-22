from django.shortcuts import render
from .models import Product

# Create your views here.


def quote(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/quote.html', context)