from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, infoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request), f'Your account has been created! You are now able to log in'
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {'form':form})

def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account updated!!!')
            request.user.profile.first = False
            return redirect('/Create')
    else:
        form = infoForm()
        first = request.user.profile.first
        if first == True:
            request.user.profile.save()
            return render(request, "users/info.html", {'form':form})
        return redirect('/') 
@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def updateprofile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/updateprofile.html', context)