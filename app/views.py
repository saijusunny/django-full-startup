from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def gall(request):
    return render(request, "gallary.html")

def abt(request):
    return render(request, "about.html")
def cnt(request):
    return render(request, "contact.html")