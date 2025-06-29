from django.urls import path
from .views import products_detail


app_name = 'products_detail'
urlpatterns = [
    path('<int:pk>', products_detail, name='products_detail'),
]