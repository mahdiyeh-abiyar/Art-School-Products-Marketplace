from django import forms

class registerForm(forms.Form):
    firstname = forms.CharField(max_length=110, widget=forms.TextInput(
        attrs={'class':'name w-full px-4 py-2 text-sm rounded-md focus:outline-none focus:ring-2 focus:ring-dark-teal bg-[#F2F4F8] shadow' 
        ,'placeholder':'نام خود را وارد کنید...'}))
    lastname = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class':'lastname w-full px-4 py-2 text-sm rounded-md focus:outline-none focus:ring-2 focus:ring-dark-teal bg-[#F2F4F8] shadow' 
               ,'placeholder':'نام خانوادگی خود را وارد کنید...'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'username w-full px-4 py-2 text-sm rounded-md focus:outline-none focus:ring-2 focus:ring-dark-teal bg-[#F2F4F8] shadow'
               ,'placeholder':'نام کاربری خود را وارد کنید.'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'email w-full px-4 py-2 text-sm rounded-md focus:outline-none focus:ring-2 focus:ring-dark-teal bg-[#F2F4F8] shadow'
               ,'placeholder':'example@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'password w-full px-4 py-2 text-sm rounded-md focus:outline-none focus:ring-2 focus:ring-dark-teal bg-[#F2F4F8] shadow' 
               ,'placeholder':'رمز خود را وارد کنید...'}))
    repassword = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'repassword w-full px-4 py-2 text-sm rounded-md focus:outline-none focus:ring-2 focus:ring-dark-teal bg-[#F2F4F8] shadow' 
               ,'placeholder':'رمز خود را وارد کنید...'}))