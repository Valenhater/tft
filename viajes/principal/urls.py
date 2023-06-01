from django.urls import path
from . import views
from .views import registrar, nuevologin, home

urlpatterns = [
    path('', registrar, name='registrar'),
    path('nuevoViaje/', views.buscarViaje, name='nuevoViaje'),
    path('confViaje/', views.vista3, name='confViaje'),
    path('registrar/', registrar, name='registrar'),
    path('nuevologin/', nuevologin, name='nuevologin'),
    path('guardarViaje/', views.guardar_viaje, name='guardarViaje'),
    # Agrega más rutas aquí
]