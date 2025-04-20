from django . shortcuts import render, redirect
from django . contrib import messages
from django . contrib.auth.models import User
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list(request):

    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    products_list = Product.objects.all()
    product_paginator = Paginator(products_list, 12)
    product_list = product_paginator.get_page(page) 
    context = {'products': product_list}
    return render(request, 'products.html', context)

def product_details(request):
    return render(request, 'product_details.html')