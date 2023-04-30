#เลขาห้องใหม่ myapp

from django.urls import path
from .views import Homepage, About, Contact, Services, Products

urlpatterns = [
    path('', Homepage,name='home'), # Localhost:8000 / www.loong.com
    path('about', About, name='about'),
    path('contact', Contact, name='contact'),
    path('services', Services, name='services'),
    path('products', Products, name='products'),
]