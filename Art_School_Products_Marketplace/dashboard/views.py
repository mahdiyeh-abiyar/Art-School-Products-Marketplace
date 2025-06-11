from django.shortcuts import render, redirect


def dashboard_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    context = {
        'hide_footer': True
    }
    return render(request, 'dashboard/Dashboard.html', context)

def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    context = {
        'hide_footer': True
    }
    return render(request, 'dashboard/user_dashboard.html', context)

def order_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    context = {
        'hide_footer': True
    }
    return render(request, 'dashboard/order.html', context)

def Favorites_page(request):
    if not request.user.is_authenticated:
        return redirect('login:login_page')
    context = {
        'hide_footer': True
    }
    return render(request, 'dashboard/Favorites.html', context)