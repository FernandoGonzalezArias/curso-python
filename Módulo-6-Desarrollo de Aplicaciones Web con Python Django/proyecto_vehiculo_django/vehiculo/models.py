from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    MARCAS_VEHICULOS =[
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota')
    ]
    
    marca = models.CharField(max_length=200, choices=MARCAS_VEHICULOS, blank=True, default='Ford')
    
    CATEGORIA_VEHICULOS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga')
        
    ]
    
    categoria = models.CharField(max_length=200, choices=CATEGORIA_VEHICULOS, blank=True, default='Particular')
    
    
    modelo= models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    precio = models.FloatField(max_length=20)
    fecha_de_creacion = models.DateField()
    fecha_de_modificacion = models.DateField()
    
    class Meta:
        ordering = ["marca"]
        
    def get_absolute_url(self):
        return reverse('vehiculo', args=[str(self.id)])
    
    def __str__(self):
        return f"Modelo: {self.modelo}"
