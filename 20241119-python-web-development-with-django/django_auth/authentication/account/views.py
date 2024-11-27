from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

def home_view(request):
    return render(request, "home.html", { "message": "Hello Home" })

def landing_view(request):
    return render(request, "home.html", { "message": "Hello Landed" })

def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("home")
        else:
            messages.error(request, "Invalid information")
    
    form = NewUserForm()
    return render(request, "register.html", { "registration_form": form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render(request, "login.html", { "login_form": form })

def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("landing")