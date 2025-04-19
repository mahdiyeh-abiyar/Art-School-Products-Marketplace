from django.shortcuts import render


def products_detail(request):
    return render(request, 'products_detail/detail.html')
