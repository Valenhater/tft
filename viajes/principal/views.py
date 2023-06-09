#from django.shortcuts import get_list_or_404, render
from .models import Destino, Alojamiento, Desplazamiento, Paquete, Viaje, Foto
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import RegisterForm
from django.db.models import Q
import stripe
from django.conf import settings
from datetime import datetime
from stripe.error import CardError

@login_required
def buscarViaje(request):
   dest = Destino.objects.all()
   context = {
        'destinos': dest,
    }
   plantilla = loader.get_template('viaje_search.html')
   return HttpResponse(plantilla.render(context, request))


@login_required
def confViaje(request):
    dest = Destino.objects.all()
    alo = Alojamiento.objects.filter(destino__nombre=request.POST['destino'], nhuespedes__gte=request.POST['viajeros']).prefetch_related('foto_set')
    despOrigen = Desplazamiento.objects.filter(origen__nombre=request.POST['origen'], destino__nombre=request.POST['destino'])
    despDestino = Desplazamiento.objects.filter(origen__nombre=request.POST['destino'], destino__nombre=request.POST['origen'])
    paq = Paquete.objects.filter(destino__nombre=request.POST['destino'])
    nHuespedes = request.POST['viajeros']
    salida = request.POST['salida']
    llegada = request.POST['llegada']

    fecha_inicio = datetime.strptime(salida, '%Y-%m-%d').date()
    fecha_fin = datetime.strptime(llegada, '%Y-%m-%d').date()
    duracion_estancia = (fecha_fin - fecha_inicio).days
    precio_total = []
    for a in alo:
        precio_total.append(duracion_estancia * a.precio)
    

    context = {
        'destinos': dest,
        'alojamientos': alo,
        'desplazamientosOrigen': despOrigen,
        'desplazamientosDestino': despDestino,
        'paquetes': paq,
        'nHuespedes': nHuespedes,
        'salida': salida,
        'llegada': llegada,
        'dias': duracion_estancia,
        'precio_total': precio_total,

    }

    plantilla = loader.get_template('viaje_vista2.html')
    return HttpResponse(plantilla.render(context, request))

def home(request):
    # Lógica de la vista home
    return render(request, 'viaje_vista2.html')

def registrar(request):
    if request.user.is_authenticated:
        return redirect('buscarViaje')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../nuevologin')  # Utiliza reverse para generar la URL de la vista 'home'
    else:
        form = RegisterForm()
    return render(request, 'registrar.html', {'form': form})

def nuevologin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../buscarViaje')  # Utiliza reverse para generar la URL de la vista 'home'
        else:
            print(password,username,user)
            return render(request, 'nuevologin.html')
    return render(request, 'nuevologin.html')

def logout_view(request):
    logout(request)
    return redirect('registrar')

@login_required
def guardar_viaje(request):
    if request.method == 'GET':
        # Obtener los datos del formulario
        alojamiento_id = request.GET.get('alojamiento')
        desp_ida_id = request.GET.get('despIda')
        desp_vuelta_id = request.GET.get('despVuelta')
        n_huespedes = request.GET.get('nHuespedes')
        salida = request.GET.get('salida')
        llegada = request.GET.get('llegada')
        pagado = request.GET.get('pagado')
        precioTotal = request.GET.get('precioTotal')

        # Obtener el usuario logueado
        usuario = request.user

        # Crear una instancia del modelo Viaje con los datos recibidos y el usuario logueado
        viaje = Viaje(
            usuario=usuario,
            alojamiento_id=alojamiento_id,
            desplazamientoIda_id=desp_ida_id,
            desplazamientoVuelta_id=desp_vuelta_id,
            nHuespedes=n_huespedes,
            salida=salida,
            llegada=llegada,
            pagado=pagado,
            precioTotal=precioTotal,
        )

        # Guardar el viaje en la base de datos
        viaje.save()

        # Guardar el ID del viaje en la sesión
        session = SessionStore(request.session.session_key)
        session['viaje_id'] = viaje.id
        session.save()

        # Redirigir a la vista de pago
        return redirect('payment')

    return render(request, 'formulario.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def verViajes(request):
    # Obtén el usuario logueado
    usuario = request.user
    # Obtén los viajes del usuario
    viajes = Viaje.objects.filter(usuario=usuario, pagado=1)
    # Renderiza el template con los datos de los viajes
    return render(request, 'verViajes.html', {'viajes': viajes})

@login_required
def detalle_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, id=id)
    return render(request, 'detalle_alojamiento.html', {'alojamiento': alojamiento})

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@login_required
def payment_view(request):
    # Obtener el ID del viaje de la sesión
    session = SessionStore(request.session.session_key)
    viaje_id = session.get('viaje_id')

    # Verificar si el ID del viaje está presente en la sesión
    if viaje_id is None:
        # El ID del viaje no está en la sesión, manejar el error o redirigir a una página apropiada
        return redirect('error')

    try:
        # Obtener el objeto Viaje por su ID
        viaje = Viaje.objects.get(id=viaje_id)

        # Realizar cualquier lógica adicional necesaria antes del pago

        # Renderizar el template de pago y pasar el objeto Viaje como variable de contexto
        return render(request, 'payment.html', {'viaje': viaje})

    except Viaje.DoesNotExist:
        # El objeto Viaje no existe, manejar el error o redirigir a una página apropiada
        return redirect('error')

@login_required
def marcar_viaje_como_pagado(request, viaje_id):
    if request.method == 'POST':
        try:
            # Obtén el objeto Viaje por su ID
            viaje = Viaje.objects.get(id=viaje_id)

            # Actualiza el campo 'pagado' a True
            viaje.pagado = True

            # Procesar el pago utilizando la biblioteca de Stripe
            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
            charge = stripe.Charge.create(
                amount=int(viaje.precioTotal * 100),  # Convertir a entero y montar en centavos
                currency='usd',  # Moneda (actualiza según tu configuración)
                source=request.POST['stripeToken'],  # Token de tarjeta enviado desde el formulario
                description='Pago del viaje: {}'.format(viaje.id)
            )

            # Guarda los cambios en la base de datos
            viaje.save()

            # Redirige a la vista de verViajes
            return redirect('verViajes')

        except Viaje.DoesNotExist:
            # El objeto Viaje no existe, maneja el error o redirige a una página apropiada
            return redirect('error')

        except CardError as e:
            # Captura la excepción de CardError y pasa el mensaje de error al template
            error_message = e.user_message
            return render(request, 'payment.html', {'viaje': viaje, 'error': error_message})

    return redirect('error')



