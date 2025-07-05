from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/', include('registr.urls')),
    path('about/', include('about.urls')),
    path('login/', include('login.urls')),
    path('products/', include('products.urls')),
    path('products_detail/', include('products_detail.urls')),
    path('product_cards/', include('productCard.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('rules/', include('rules.urls')),
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
