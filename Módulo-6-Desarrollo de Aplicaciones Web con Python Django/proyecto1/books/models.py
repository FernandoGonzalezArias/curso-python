from django.db import models
from django.urls import reverse


class Book(models.Model):
    
    titulo = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    
    STATUS = (
        ('a', 'Activo'),
        ('m', 'Mantenimiento'),
        ('r', 'Reservado')
    )
    state = models.CharField(max_length=1, choices=STATUS, blank=True, default='a')
    
    TIPOS_BOOK = [
        ('p', 'Pasta'),
        ('D', 'Digital')
    ]
    
    type = models.CharField(max_length=1, choices=TIPOS_BOOK, blank=True, default='P')

    class Meta:
        ordering = ["titulo"]
        
    def get_absoluted_url(self):
        return reverse('book', args=[str(self.id)])
        
    def __str__(self):
        return f"titulo: {self.titulo}, editorial: {self.editorial}"