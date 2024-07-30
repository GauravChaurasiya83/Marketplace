from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category,Item

admin.site.register(Category)
admin.site.register(Item)

