from django.shortcuts import render
from products.models import Product

def products_detail(request, pk):
    id = Product.objects.get(id=pk)
    context = {"id": id}
    return render(request, 'products_detail/detail.html', context)