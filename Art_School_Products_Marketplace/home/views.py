from django.shortcuts import render
from products.models import Product


def home_page(request):
    products = Product.objects.filter(is_show=True)[:4]
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)

