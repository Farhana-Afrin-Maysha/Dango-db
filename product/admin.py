from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','image']


admin.site.register(Product,ProductAdmin )
