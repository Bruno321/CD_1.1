from django.contrib import admin
from .models import Cancion,Album,Generos,Disquera,PlayList,PlayListCanciones,UsuarioCanciones

# Register your models here.
admin.site.register(Cancion)
admin.site.register(Generos)
admin.site.register(Disquera)
admin.site.register(PlayList)
admin.site.register(PlayListCanciones)
admin.site.register(UsuarioCanciones)
admin.site.register(Album)
