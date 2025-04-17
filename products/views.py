from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'products.html')

def product_details(request):
    return render(request, 'product_details.html')