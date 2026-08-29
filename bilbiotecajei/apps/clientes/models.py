from django.db import models

# Create your models here.

class Rol (models.Model):
    name = models.CharField  (null=True, max_length=50)
    
    def __str__(self):
        return f'{self.name}'

class Clientes (models.Model):
    name = models.CharField  (null=True, max_length=50)
    last_name = models.CharField  (null=True, max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} - {self.rol}'