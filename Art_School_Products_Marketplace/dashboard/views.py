from django.shortcuts import render


def dashboard_page(request):
    return render(request, 'dashboard/Dashboard.html')

def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

def order_page(request):
    return render(request, 'dashboard/order.html')

def Favorites_page(request):
    return render(request, 'dashboard/Favorites.html')