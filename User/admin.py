from django.contrib import admin

# Register your models here.
from .models import User,Post
admin.register(User, Post)(admin.ModelAdmin)
