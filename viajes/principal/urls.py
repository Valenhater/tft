from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista1, name='viaje_list.html'),
    path('ruta2/', views.vista2, name='viaje_vista2.html'),
    # Agrega más rutas aquí
]