from django.urls import path
from .views import Digital_design, Painting_illustration, photography, printed_product, Website_design


app_name = 'productCard'
urlpatterns = [
    path('Digital_design/', Digital_design, name='Digital_design'),
    path('Painting_illustration/', Painting_illustration, name='Painting_illustration'),
    path('photography/', photography, name='photography'),
    path('printed_product/', printed_product, name='printed_product'),
    path('Website_design/', Website_design, name='Website_design'),
]