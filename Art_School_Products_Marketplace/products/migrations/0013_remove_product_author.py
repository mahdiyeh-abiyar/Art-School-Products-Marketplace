# Generated by Django 5.2 on 2025-06-30 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
    ]
