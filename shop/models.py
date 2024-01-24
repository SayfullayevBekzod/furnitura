from django.db import models

# Create your models here.

class Home(models.Model):
    foto = models.ImageField(default='couch.png')
    name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    foto = models.ImageField(default='couch.png')
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name
    
class ProductList(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
    
class Shop(models.Model):
    foto = models.ImageField(default='couch.png')
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name
    
class Choose(models.Model):
    foto = models.ImageField(default='couch.png')
    title = models.CharField(max_length=20, null=True, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    
class Team(models.Model):
    foto = models.ImageField(default='couch.png')
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    job = models.CharField(max_length=20, null=True, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.first_name
    
class More(models.Model):
    foto = models.ImageField(default='couch.png')
    type = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name