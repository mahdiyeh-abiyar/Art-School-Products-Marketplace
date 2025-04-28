from django.db import models

class productCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title