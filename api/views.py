from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import User

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def SignUpView(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Register successful"))
            return redirect('login')
    return render(request, 'api/spa/signup.html', {'form':form})

def LogInView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Email or Password is incorrect')
            return redirect('login')
    return render(request, 'api/spa/login.html', {})

def LogoutView(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('login')

def getUser(request):
    user = request.user

    user_data = {
        'email': user.email,
        'birthdate': user.birthdate,
    }

    return JsonResponse(user_data)