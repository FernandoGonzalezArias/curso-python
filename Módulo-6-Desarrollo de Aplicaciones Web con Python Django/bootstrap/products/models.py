from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return f'{self.name}'
