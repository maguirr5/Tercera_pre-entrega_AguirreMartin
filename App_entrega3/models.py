from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    edad = models.models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido} , {self.edad} "


class ArteMarcial(models.Model):
    estilo = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    zona = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.estilo} {self.pais} , {self.zona}"


class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    duracion = models.IntegerField()
    def __str__(self):
       return f"{self.titulo} {self.director} , {self.duracion}"