from django.contrib import admin

#Register your models here.
from .models import Viaje, Paquete

admin.site.register(Viaje)
admin.site.register(Paquete)