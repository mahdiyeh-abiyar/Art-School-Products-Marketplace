from django.contrib import admin
from .models import Product,category

class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_show']
    search_fields = ['title', 'description', 'category']
    list_filter = ['is_show', 'category']

admin.site.register(Product, AdminProduct)
admin.site.register(category)
