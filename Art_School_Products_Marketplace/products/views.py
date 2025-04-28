from django.shortcuts import render
from products.models import Product


def products_page(request):
    products = Product.objects.filter(is_show=True)
    search_key = request.GET.get('search')
    if search_key:
        products = products.filter(title__icontains=search_key)
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)
