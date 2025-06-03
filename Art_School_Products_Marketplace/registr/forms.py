from django import forms
from django.contrib.auth. models import User
from django.core.exceptions import ValidationError

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
    

    def clean_username(self):
        username_input = self.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username_input).exists()
        if user_exists:
            raise ValidationError('نام کاربری وارد شده قبلاً ثبت شده است. لطفاً نام دیگری انتخاب کنید.')
        return username_input
    
    def clean_repassword(self):
        password_input = self.cleaned_data.get('password')
        repassword_input = self.cleaned_data.get('repassword')
        if password_input != repassword_input:
            raise ValidationError('رمز عبور و تکرار آن یکسان نیستند.')
        return repassword_input
    
    def clean_email(self):
        email_input = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email= email_input).exists()
        if email_exists:
            raise ValidationError('این ایمیل قبلاً وارد شده است. لطفاً ایمیل دیگری وارد کنید.')
        return email_input


