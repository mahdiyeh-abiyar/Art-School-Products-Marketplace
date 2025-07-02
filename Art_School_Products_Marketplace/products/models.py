from django.db import models

class category(models.Model):
    title = models.CharField(max_length= 100, help_text="عنوان دسته بندی",null=True , blank=True )
    url_name = models.CharField(max_length=100, help_text="این عنوان برای آدرس دهی دسته بندی ها استفاده میشود, پس از این اسم حتما باید در آدرس دهی استفاده کنید.", null=True , blank=True)

    def __str__(self):
        return self.title 

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True , blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE ,null=True , blank=True)
    is_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title