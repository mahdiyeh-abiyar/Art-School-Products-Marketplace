from django.shortcuts import render


def products_page(request):
    return render(request, 'products/products.html')
