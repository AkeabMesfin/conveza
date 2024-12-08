from django.shortcuts import render, redirect
from . models import User
from . forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('feed')
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
  
    return render(request, 'authen/sign-up.html', {'form': form})



def login(request):
    if request.user.is_authenticated:
        return redirect('feed')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('feed')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'authen/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')