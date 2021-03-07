from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response), f'Your account has been created! You are now able to log in'
        return redirect('/login')
    else:
        form = RegisterForm()
    return render(response, "users/register.html", {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')