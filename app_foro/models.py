
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class publicacion(models.Model):
    usuario = models.CharField(max_length=40)
    tema_especifico = models.CharField(max_length=50)
    consulta = models.TextField() 
    fecha_de_publicacion = models.DateField(default=datetime.now())



class contacto(models.Model):
    usuario = models.CharField(max_length=40)
    email = models.EmailField()
    razon_contacto = models.TextField()
    fecha_de_contacto = models.DateField(default=datetime.now())



class sorteo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()


class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares' , null=True , blank = True)


class comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    publicacion_comentada = models.ForeignKey(publicacion, on_delete=models.CASCADE) 




