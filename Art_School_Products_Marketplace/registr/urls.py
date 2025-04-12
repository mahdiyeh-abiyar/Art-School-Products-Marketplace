from django.urls import path
from .views import registr_page


app_name = 'registr'
urlpatterns = [
    path('', registr_page, name='registr_page')
]