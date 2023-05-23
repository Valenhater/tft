from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista1, name='viaje_list.html'),
    path('ruta2/', views.vista2, name='nombre_vista2'),
    # Agrega más rutas aquí
]