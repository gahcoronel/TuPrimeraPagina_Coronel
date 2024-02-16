from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    ciudad = models.CharField(max_length=30)

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    sucursal = models.IntegerField()

class Producto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    costo = models.FloatField()
    stock = models.IntegerField()
    
