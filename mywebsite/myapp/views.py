from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Product

def Homepage(request):
    product = Product.objects.all()
    context = {'product':product}    
    return render(request, 'myapp/home.html',context)

def About(request):
    return render(request, 'myapp/about.html')

def Contact(request):
    namelist = Staff.objects.all()
    context = {'namelist':namelist}
    return render(request, 'myapp/contact.html',context)

def Services(request):
    return render(request, 'myapp/services.html')

def Products(request):
    return render(request, 'myapp/products.html')
