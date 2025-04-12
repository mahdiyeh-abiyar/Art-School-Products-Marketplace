from django.shortcuts import render
from .models import Products


def Products_list(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)

