from django.db import models

# Create your models here.

class Categoria (models.Model):
    name = models.CharField  (null=True, max_length=50)
    
    def __str__(self):
        return f'{self.name}'

class Productos (models.Model):
    name = models.CharField  (null=True, max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} - {self.categoria}'