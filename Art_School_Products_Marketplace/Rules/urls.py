from django.urls import path
from .views import rules_page


app_name = 'rules'
urlpatterns = [
    path('', rules_page, name='rules_page')
]