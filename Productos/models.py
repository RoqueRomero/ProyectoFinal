from django.db import models

# Create your models here.
class Item(models.Model):
    nombre=models.CharField(max_length=40)
    marca=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=70)
    
def __str__(self):
    return self.nombre
