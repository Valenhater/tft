from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True,null=False)
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
    idAlojamiento = models.AutoField(primary_key=True,null=False)
    nombre  = models.CharField(max_length=200)
    descripcion = models.FloatField()
    nhabitaciones = models.IntegerField()
    nbanos = models.IntegerField()
    nhuespuedes = models.IntegerField()
    direccion = models.CharField(max_length=200)
    precio = models.FloatField()
    fotos = models.CharField(max_length=200)

    class Meta:
        verbose_name='alojamiento'
        verbose_name_plural="alojamientos"
        ordering=['-created']

    def __str__(self):
        return self.modelo

class Desplazamiento(models.Model): 
    idDesplazamiento = models.AutoField(primary_key=True,null=False)
    vehiculo  = models.CharField(max_length=200)
    precio = models.FloatField()
    foto  = models.CharField(max_length=200)

    class Meta:
        verbose_name='desplazamiento'
        verbose_name_plural="desplazamientos"
        ordering=['-created']

    def __str__(self):
        return self.modelo

class Paquete(models.Model):
    idPaquete = models.AutoField(primary_key=True,null=False)
    descripcion  = models.TextField()
    precio = models.FloatField()
    foto  = models.CharField(max_length=200)

    class Meta:
        verbose_name='paquete'
        verbose_name_plural="paquetes"
        ordering=['-created']

    def __str__(self):
        return self.modelo
    
class Viaje(models.Model):
    idViaje = models.AutoField(primary_key=True,null=False)
    idUsuario = models.IntegerField()
    idAlojamiento = models.IntegerField()
    idPaquete = models.IntegerField()
    nHuespedes = models.FloatField()
    salida  = models.CharField(max_length=200)
    llegada  = models.CharField(max_length=200)

    class Meta:
        verbose_name='viaje'
        verbose_name_plural="viajes"
        ordering=['-created']

    def __str__(self):
        return self.modelo