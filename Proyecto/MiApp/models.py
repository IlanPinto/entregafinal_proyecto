from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

class Torneos(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    puntos_otorgados = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre}, Pais: {self.pais}"

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    entrenado = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)


class Blogs(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    fecha_imagen = models.DateField()
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    cuerpo = models.CharField(max_length=400, default='')