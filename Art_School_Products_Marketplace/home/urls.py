from django.urls import path , include
from .views import  home_page


app_name = 'home'
urlpatterns = [
    path('', home_page, name='home_page'),
]