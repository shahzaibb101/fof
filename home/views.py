from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request, "home.html")

def user_dashboard(request):
    return render(request, "user_dashboard.html")

def cms(request):
    return render(request, "cms.html")