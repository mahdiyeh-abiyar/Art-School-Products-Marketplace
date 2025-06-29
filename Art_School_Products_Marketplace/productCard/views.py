from django.shortcuts import render
from products.models import Product


def Digital_design(request):
    products = Product.objects.filter(category_id=1)
    context = {
        'products': products
    }
    return render(request, 'DigitalDesign.html', context)

def Painting_illustration(request):
    products = Product.objects.filter(category_id=2)
    context = {
        'products': products
    }
    return render(request, 'Paintingillustration.html', context)

def photography(request):
    products = Product.objects.filter(category_id=4)
    context = {
        'products': products
    }
    return render(request, 'photography.html', context)

def printed_product(request):
    products = Product.objects.filter(category_id=3)
    context = {
        'products': products
    }
    return render(request, 'PrintedProducts.html', context)

def Website_design(request):
    products = Product.objects.filter(category_id=5)
    context = {
        'products': products
    }
    return render(request, 'WebsiteDesign.html', context)