from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Coustamer
from django.contrib.auth.models import User
# Create your views here.
def logout_section(request):
    logout(request)
    return redirect('home')

def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')

            #Create User Account
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                address=address
                )
            
            #Create coustomer account

            coustamer = Coustamer.objects.create(
                user = user,
                phone=phone,
            )
            success_message = "User registration successful!"
            messages.success(request, success_message)
        except Exception as e:
            error = "This username already exists!"
            messages.error(request, error)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Inavild username or password")
    return render(request, 'account.html', context) 