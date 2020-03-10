from django.shortcuts import render

# Create your views here.
from product.models import Product


def productList(request):
   product_list_querry = Product.objects.all()
   template ='product/product-list.html'
   context ={'products':product_list_querry}
   return render(request, template, context)