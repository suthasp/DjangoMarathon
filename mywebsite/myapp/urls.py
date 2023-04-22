#เลขาห้องใหม่ myapp

from django.urls import path
from .views import Homepage

urlpatterns = [
    path('', Homepage), # Localhost:8000 / www.loong.com
]