from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Usuario(models.Model):
    nombre  = models.CharField(max_length=200,null=False)
    correo = models.EmailField(max_length=254,null=False)
    password = models.CharField(max_length=200,null=False)
    foto = models.ImageField(verbose_name='foto',upload_to='viajes')

    class Meta:
        verbose_name='usuario'
        verbose_name_plural="usuarios"
    
    def __str__(self):
        return self.nombre
    
class Destino(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto = models.ImageField(verbose_name='foto',upload_to='viajes')

    class Meta:
        verbose_name = 'destino'
        verbose_name_plural = 'destinos'

    def __str__(self):
        return self.nombre

class Alojamiento(models.Model): 
    nombre  = models.CharField(max_length=200)
    tipo  = models.CharField(max_length=200)
    descripcion = models.TextField()
    nhabitaciones = models.IntegerField()
    nbanos = models.IntegerField()
    nhuespuedes = models.IntegerField()
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    precio = models.FloatField()
    fotos = models.ImageField(verbose_name='foto',upload_to='viajes')

    class Meta:
        verbose_name='alojamiento'
        verbose_name_plural="alojamientos"

    def __str__(self):
        return self.nombre

class Desplazamiento(models.Model): 
    nombre = models.CharField(max_length=200)
    vehiculo  = models.CharField(max_length=200)
    precio = models.FloatField()
    foto  = models.ImageField(verbose_name='foto',upload_to='viajes')
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)

    class Meta:
        verbose_name='desplazamiento'
        verbose_name_plural="desplazamientos"
    
    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    nombre  = models.CharField(max_length=200)
    descripcion  = models.TextField()
    precio = models.FloatField()
    foto  = models.ImageField(verbose_name='foto',upload_to='viajes')

    class Meta:
        verbose_name='paquete'
        verbose_name_plural="paquetes"

    def __str__(self):
        return self.nombre
    
class Viaje(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    DesplazamientoIda = models.ForeignKey(Desplazamiento,related_name='viaje_ida' ,on_delete=models.CASCADE)
    DesplazamientoVuelta = models.ForeignKey(Desplazamiento,related_name='viaje_vuelta', on_delete=models.CASCADE)
    Paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    nHuespedes = models.FloatField()
    salida  = models.CharField(max_length=200)
    llegada  = models.CharField(max_length=200)

    class Meta:
        verbose_name='viaje'
        verbose_name_plural="viajes"

    def __str__(self):
        return self.nombre

