from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Coustamer
# Create your views here.

def account(request):
    if request.POST and 'register' in request.POST:
        try:

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            #Create User Account
            user = User.objects.create_user(username=username,password=password,email=email)
            #Create coustomer account
            coustamer = Coustamer.objects.create(
                user = user,
                phone=phone,
            )
            return redirect('home')
        except Exception as e:
            error = "This username already exists!"
            messages.error(request, error)
    return render(request, 'account.html') 