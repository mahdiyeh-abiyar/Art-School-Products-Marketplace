from django.db import models

class Home(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField(max_length = 10000)
    # images = models.ImageField(upload_to = ".")