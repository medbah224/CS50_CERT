from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def mohamed(request):
    return HttpResponse("Hello, Mohamed")

def great(request, name):
    return render(request, "hello/great.html", context={
        "name" : name
    })
