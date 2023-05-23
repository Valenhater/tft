from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.models.AutoField(primary_key=True,null=False)
    nombreUsuario  = models.CharField(max_length=200,null=False)
    correo = models.EmailField(max_length=254,null=False)
    password = models.CharField(max_length=200,null=False)
    foto = models.CharField(max_length=200,null=True)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural="usuarios"
        ordering=['-created']

    def __str__(self):
        return self.nombreUsuario

class Alojamiento(models.Model): 
    idAlojamiento = models.models.AutoField(primary_key=True,null=False)
    nombre  = models.CharField(max_length=200)
    descripcion = models.FloatField()
    nhabitaciones = models.IntegerField()
    nbanos = models.IntegerField()
    nhuespuedes = models.IntegerField()
    direccion = models.CharField(max_length=200)
    precio = models.FloatField()
    fotos = models.CharField(max_length=200)

    class Meta:
        verbose_name='camion'
        verbose_name_plural="camiones"
        ordering=['-created']

    def __str__(self):
        return self.modelo
