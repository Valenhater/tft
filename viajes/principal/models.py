from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser,Group, Permission
    
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
    nhuespedes = models.IntegerField()
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    precio = models.FloatField()

    class Meta:
        verbose_name='alojamiento'
        verbose_name_plural="alojamientos"

    def __str__(self):
        return self.nombre
    
class Foto(models.Model):
    foto = models.ImageField(verbose_name='foto',upload_to='viajes')
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)

    class Meta:
        verbose_name='foto'
        verbose_name_plural="fotos"

class Desplazamiento(models.Model): 
    nombre = models.CharField(max_length=200)
    vehiculo  = models.CharField(max_length=200)
    precio = models.FloatField()
    foto  = models.ImageField(verbose_name='foto',upload_to='viajes')
    origen = models.ForeignKey(Destino, related_name='viaje_origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, related_name='viaje_destino', on_delete=models.CASCADE)
    

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
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)

    class Meta:
        verbose_name='paquete'
        verbose_name_plural="paquetes"

    def __str__(self):
        return self.nombre
    
#bbdd del login
class CustomUser(AbstractUser):
    # Otros campos de tu modelo CustomUser

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set'  # Agrega related_name aquí
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set'  # Agrega related_name aquí
    )


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Agrega campos adicionales para el perfil

class Viaje(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    desplazamientoIda = models.ForeignKey(Desplazamiento,related_name='viaje_ida' ,on_delete=models.CASCADE, blank=True)
    desplazamientoVuelta = models.ForeignKey(Desplazamiento,related_name='viaje_vuelta', on_delete=models.CASCADE, blank=True)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE,blank=True, null=True)
    nHuespedes = models.FloatField()
    salida  = models.DateField()
    llegada  = models.DateField()
    pagado = models.BooleanField()
    class Meta:
        verbose_name='viaje'
        verbose_name_plural="viajes"

    def __str__(self):
        return self.nombre