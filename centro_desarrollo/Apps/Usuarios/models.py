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

class Album(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    duracion = models.DecimalField(max_digits=4, decimal_places=2,null=True) 
    fecha = models.DateField(auto_now=False ,auto_now_add=False)
    foto = models.ImageField(upload_to=4,max_length=100)

class PlayList(models.Model):
    is_public = models.BooleanField()
    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

class PlayListCanciones(models.Model):
    playlist = models.ForeignKey('PlayList',on_delete=models.CASCADE)
    cancion = models.ForeignKey('Cancion',on_delete=models.CASCADE)
