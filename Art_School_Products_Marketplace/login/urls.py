from django.urls import path
from .views import login_page


app_name = 'login'
urlpatterns = [
    path('', login_page, name='login_page')
]