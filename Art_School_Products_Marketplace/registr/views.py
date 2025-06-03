from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def registr_page(request):
    print("POST received")
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_page')
    useregisterForm = registerForm()
    if request.method == 'POST':
        useregisterForm = registerForm(data=request.POST)
        if useregisterForm.is_valid():
            firstname = useregisterForm.cleaned_data.get('firstname')
            lastname  = useregisterForm.cleaned_data.get('lastname')
            username  = useregisterForm.cleaned_data.get('username')
            email     = useregisterForm.cleaned_data.get('email')
            repassword  = useregisterForm.cleaned_data.get('repassword')

            user = User.objects.create_user( username=username, password= repassword )
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()
            login(request, user)
            return redirect('login:login_page')
    else:
        useregisterForm = registerForm()

    print(useregisterForm.errors)
    context = {'useregisterForm': useregisterForm}
    return render(request, 'registr/Registr.html', context)


