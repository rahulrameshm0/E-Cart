from django . shortcuts import render, redirect
from django . contrib import messages
from django . contrib.auth.models import User
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_products = Product.objects.order_by('priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context = {
       'featured_products':featured_products,
       'latest_products':latest_products 
    }
    return render(request, 'index.html', context)

def product_list(request): 

    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    products_list = Product.objects.order_by('priority')
    product_paginator = Paginator(products_list, 2)
    product_list = product_paginator.get_page(page) 
    context = {'products': product_list}
    return render(request, 'products.html', context)

def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product':product}
    return render(request, 'product_details.html', context)