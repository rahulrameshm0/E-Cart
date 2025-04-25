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

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username already exists!")
                return render(request, 'account.html', context)

            # Create User
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )

            # Create Coustamer with extra fields
            coustamer = Coustamer.objects.create(
                user=user,
                phone=phone,
                address=address 
            )

            messages.success(request, "User registration successful!")

        except Exception as e:
            messages.error(request, f"Registration failed: {e}")

    elif request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'account.html', context)