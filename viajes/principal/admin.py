from django.contrib import admin

#Register your models here.
from .models import Viaje, Paquete, Destino, Alojamiento, Desplazamiento, Foto, CustomUser

admin.site.register(Destino)
admin.site.register(Foto)
admin.site.register(Viaje)
admin.site.register(Paquete)
admin.site.register(Alojamiento)
admin.site.register(Desplazamiento)
admin.site.register(CustomUser)
