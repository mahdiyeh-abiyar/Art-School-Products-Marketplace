from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', include('registr.urls')),
    path('about/', include('about.urls')),
    path('login/', include('login.urls')),
    path('products/', include('products.urls')),
]
