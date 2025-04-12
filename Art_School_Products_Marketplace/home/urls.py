from django.urls import path , include
from .views import  Products_list


app_name = 'home'
urlpatterns = [
    path('', Products_list, name='Products_list'),
    # path('home/registr/', include('registr.urls')),
]