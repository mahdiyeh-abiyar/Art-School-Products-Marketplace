from django.urls import path
from .views import login_page, logout_page


app_name = 'login'
urlpatterns = [
    path('', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
]