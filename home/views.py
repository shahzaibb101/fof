from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request, "home.html")

def user_dashboard(request):
    return render(request, "user_dashboard.html")

def cms(request):
    return render(request, "cms.html")

def sign_in(request):
    return render(request, "sign_in.html")

def sign_up(request):
    return render(request,"sign_up.html")