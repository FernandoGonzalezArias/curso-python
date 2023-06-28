from django.db import models
from django.urls import reverse


class Book(models.Model):
    
    titulo = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
   
    class Meta:
        ordering = ["titulo"]
        
    def get_absoluted_url(self):
        return reverse('book', args=[str(self.id)])
        
    def __str__(self):
        return f"titulo: {self.titulo}, editorial: {self.editorial}"