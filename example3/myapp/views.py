from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    if request.user.is_authenticated:
        messages.success(request, 'You have successfully logged in!')
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('profile')
        else:
            messages.error(request, 'Login failed: Please check your username and password.')
    return render(request, 'login.html')
