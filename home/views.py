from django.shortcuts import render, redirect
from authen.models import User
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'home/home.html')

def privacy_policy(request):
    return render(request, 'home/privacy-policy.html')

def term_conditions(request):
    return render(request, 'home/term-conditions.html')