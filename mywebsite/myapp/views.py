from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request, 'myapp/home.html')

def About(request):
    return render(request, 'myapp/about.html')

def Contact(request):
    return render(request, 'myapp/contact.html')

def Services(request):
    return render(request, 'myapp/services.html')

def Products(request):
    return render(request, 'myapp/products.html')
