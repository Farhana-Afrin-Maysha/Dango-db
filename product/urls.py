# from django.contrib import admin
# from django.conf import settings
from django.urls import path, include
# from django.conf.urls.static import static

from product.views import productList

urlpatterns = [
    path('productlist/', productList),
]
