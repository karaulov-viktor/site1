import django.contrib.admin
from django.contrib import admin
from page.models import Category, Good
django.contrib.admin.register,
admin.site.register(Category)
admin.site.register(Good)

# Register your models here.
