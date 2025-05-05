from django.shortcuts import render
from django.db.models import Q
from products.models import Product, category

def products_page(request):

    search_query = request.GET.get('search')
    if search_query:
        products = Product.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query),
            is_show=True
        )
        context = {
            'products': products,
            'search_query': search_query
        }
    else:
        all_products = Product.objects.filter(is_show=True)
        categories = category.objects.all()
        data = []

        for cat in categories:
            products = Product.objects.filter(category=cat, is_show=True)
            if products.exists():
                data.append({
                    'category': cat,
                    'products': products
                })

        context = {
            'categories_with_products': data,
            'products': all_products
        }
    return render(request, 'products/products.html', context)

