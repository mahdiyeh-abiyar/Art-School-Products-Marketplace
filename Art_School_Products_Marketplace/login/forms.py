from django import forms

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'phone w-full px-4 py-2 text-sm rounded-md focus:outline-none  bg-[#F2F4F8] shadow'
               ,'placeholder':'نام کاربری خود را وارد کنید.'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'password w-full px-4 py-2 text-sm rounded-md focus:outline-none bg-[#F2F4F8] shadow'
               , 'placeholder':'رمز خود را وارد کنید...'}))
    
    
    