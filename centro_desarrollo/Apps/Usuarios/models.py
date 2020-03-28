import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


def images_path():
    return os.path.join(settings.STATICFILES_DIRS,'img/disc_photos')

# Create your models here.
class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.DecimalField(max_digits=4, decimal_places=2)
    autor = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=4,decimal_places=2, null=True)
    album = models.ForeignKey('Album',on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.nombre,self.album)

    class Meta:
        verbose_name="Cancion"
        verbose_name_plural="Canciones"

class Album(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    duracion = models.DecimalField(max_digits=4, decimal_places=2,null=True) 
    fecha = models.DateField(auto_now=False ,auto_now_add=False)
    foto = models.ImageField(upload_to=images_path,max_length=100)

    def __str__(self):
        return self.nombre

class PlayList(models.Model):
    is_public = models.BooleanField()
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)

class PlayListCanciones(models.Model):
    playlist = models.ForeignKey('PlayList',on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion',on_delete=models.CASCADE)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name="UsuarioCanciones"
        verbose_name_plural="UsuariosCanciones"

class Disquera(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

class UsuarioCanciones(models.Model):
    id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    id_cancion = models.ForeignKey('Cancion',on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
        
class Generos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField()
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=100)
    foto = models.ImageField(upload_to=images_path,max_length=100)
    is_artist = models.BooleanField()