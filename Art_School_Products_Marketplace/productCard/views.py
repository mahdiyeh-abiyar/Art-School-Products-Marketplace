from django.shortcuts import render
# from productCard.views import productCard


def Digital_design(request):
    return render(request, 'productCards/Digital-design.html')

def Painting_illustration(request):
    return render(request, 'productCards/Painting-illustration.html')

def photography(request):
    return render(request, 'productCards/photography.html')

def printed_product(request):
    return render(request, 'productCards/printed-product.html')

def Website_design(request):
    return render(request, 'productCards/Website-design.html')
