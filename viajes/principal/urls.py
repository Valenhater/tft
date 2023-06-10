from django.urls import path
from . import views
from .views import registrar, nuevologin, error_404_view, payment_view

handler404 = error_404_view

urlpatterns = [
    path('', registrar, name='registrar'),
    path('buscarViaje/', views.buscarViaje, name='buscarViaje'),
    path('verViajes/', views.verViajes, name='verViajes'),
    path('confViaje/', views.confViaje, name='confViaje'),
    path('registrar/', registrar, name='registrar'),
    path('nuevologin/', nuevologin, name='nuevologin'),
    path('guardarViaje/', views.guardar_viaje, name='guardarViaje'),
    path('logout/', views.logout_view, name='logout'),
    path('alojamiento/<int:id>/', views.detalle_alojamiento, name='detalle_alojamiento'),
    path('viaje/<int:id>/', views.detalle_viaje, name='detalle_viaje'),
    path('payment/', payment_view, name='payment'),
    path('marcarViajeComoPagado/<int:viaje_id>/', views.marcar_viaje_como_pagado, name='marcarViajeComoPagado'),
    # Agrega más rutas aquí
]