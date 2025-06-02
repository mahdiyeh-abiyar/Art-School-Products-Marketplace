from django.urls import path
from .views import  dashboard_page, user_dashboard, Favorites_page, order_page


app_name = 'dashboard'
urlpatterns = [
    path('', dashboard_page, name='dashboard_page'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('Favorites_page/', Favorites_page, name='Favorites_page'),
    path('order_page/', order_page, name='order_page'),
]