from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    weight = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
