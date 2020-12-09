from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.CharField(max_length=10)

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=30)
    precio=models.IntegerField()

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
