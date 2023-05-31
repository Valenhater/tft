from django.urls import path
from . import views
from .views import registrar, nuevologin, home

urlpatterns = [
    path('', registrar, name='registrar'),
    path('nuevoViaje', views.vista1, name='viaje_list.html'),
    path('confViaje/', views.vista3, name='confViaje'),
    path('registrar/', registrar, name='registrar'),
    path('nuevologin/', nuevologin, name='nuevologin'),
    path('', home, name='home'),
    # Agrega más rutas aquí
]