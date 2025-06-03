from django.shortcuts import render, redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout


def login_page(request):

    if request.user.is_authenticated :
        return redirect('dashboard:dashboard_page')

    if request.method == 'POST':
        userloginForm = loginForm(request.POST)
        if userloginForm.is_valid():
            username = userloginForm.cleaned_data.get('username')
            password = userloginForm.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard_page')
            else:
                userloginForm.add_error('password', 'نام کاربری یا رمز عبور شما اشتباه است.')
    else:
        userloginForm = loginForm()

    context = {'userloginForm': userloginForm}
    return render(request, 'login/login.html', context)

def logout_page(request):
    logout(request)
    return redirect('home:home_page')