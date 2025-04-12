from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(help_text="Plase Enter Your Text Here ", max_length=10000)
    
    def __str__(self):
        return self.title
