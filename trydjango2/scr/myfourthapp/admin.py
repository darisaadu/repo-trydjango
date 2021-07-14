from django.contrib import admin

# Register your models here.

from .models import MyProduct


# class MyProductAdmin(admin.ModelAdmin):
# 	list_display = ['title', 'content','price', 'summary']


admin.site.register(MyProduct)