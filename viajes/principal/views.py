#from django.shortcuts import get_list_or_404, render
from .models import Destino, Alojamiento, Desplazamiento, Paquete, Viaje, Foto
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import RegisterForm
from django.db.models import Q
from datetime import datetime

@login_required
def buscarViaje(request):
   dest = Destino.objects.all()
   context = {
        'destinos': dest,
    }
   plantilla = loader.get_template('viaje_search.html')
   return HttpResponse(plantilla.render(context, request))

# def vista2(request):
#     dest = Destino.objects.all()
#     alo = Alojamiento.objects.all()
#     desp = Desplazamiento.objects.all()
#     paq = Paquete.objects.all()
#     via = Viaje.objects.all()

#     context = {
#         'destinos': dest,
#         'alojamientos': alo,
#         'desplazamientos': desp,
#         'paquetes': paq,
#         'viajes': via,
#     }
#     plantilla = loader.get_template('viaje_vista2.html')
#     return HttpResponse(plantilla.render(context, request))

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
            llegada=llegada
        )

        # Guardar el viaje en la base de datos
        viaje.save()

        # Redirigir a una página de éxito o a otra vista
        return redirect('../verViajes')

    return render(request, 'formulario.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def verViajes(request):
    # Obtén el usuario logueado
    usuario = request.user
    # Obtén los viajes del usuario
    viajes = Viaje.objects.filter(usuario=usuario)
    # Renderiza el template con los datos de los viajes
    return render(request, 'verViajes.html', {'viajes': viajes})

@login_required
def detalle_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, id=id)
    return render(request, 'detalle_alojamiento.html', {'alojamiento': alojamiento})