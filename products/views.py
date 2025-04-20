from django . shortcuts import render, redirect
from django . contrib import messages
from django . contrib.auth.models import User
from . models import Product
# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list(request):
    products_list = Product.objects.all()
    context = {'products': products_list}
    return render(request, 'products.html', context)

def product_details(request):
    return render(request, 'product_details.html')