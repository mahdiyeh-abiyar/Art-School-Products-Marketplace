from django.shortcuts import render, redirect


def dashboard_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    return render(request, 'dashboard/Dashboard.html')

def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    return render(request, 'dashboard/user_dashboard.html')

def order_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    return render(request, 'dashboard/order.html')

def Favorites_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    return render(request, 'dashboard/Favorites.html')