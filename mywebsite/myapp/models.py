from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class Staff(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name