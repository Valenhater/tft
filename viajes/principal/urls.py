from django.urls import path
from . import views

urlpatterns = [
    #path('', views.vista1, name='viaje_list.html'),
    path('', views.vista2, name=''),
    path('confViaje/', views.vista3, name='confViaje')
    # Agrega más rutas aquí
]