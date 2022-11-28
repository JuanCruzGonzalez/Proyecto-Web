from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    camada=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre.upper()} --> Camada:{self.camada}"
class profesores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.email} {self.profesion}"
class estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} | Mail: {self.email}"
class entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self) -> str:
        return f"{self.nombre} {self.fecha_de_entrega} {self.entregado}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", null=True, blank=True)