from django.shortcuts import render


def registr_page(request):
    return render(request, 'registr/Registr.html')
