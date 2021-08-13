from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
