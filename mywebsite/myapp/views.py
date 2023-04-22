from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return HttpResponse('<h1>Hello Website by Django</h1>')
