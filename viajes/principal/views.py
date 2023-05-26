#from django.shortcuts import get_list_or_404, render
from .models import Destino, Alojamiento, Desplazamiento, Paquete, Viaje
#from django.http import HttpResponse
#from django.template import loader
#from django.views.generic.list import request
#from django.views.generic.detail import DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse, reverse_lazy
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def vista1(request):
   dest = Destino.objects.all()
   context = {
        'destinos': dest,
    }
   plantilla = loader.get_template('viaje_list.html')
   return HttpResponse(plantilla.render(context, request))

def vista2(request):
    dest = Destino.objects.all()
    alo = Alojamiento.objects.all()
    desp = Desplazamiento.objects.all()
    paq = Paquete.objects.all()
    via = Viaje.objects.all()

    context = {
        'destinos': dest,
        'alojamientos': alo,
        'desplazamientos': desp,
        'paquetes': paq,
        'viajes': via,
    }
    plantilla = loader.get_template('viaje_vista2.html')
    return HttpResponse(plantilla.render(context, request))

def vista3(request):
    dest = Destino.objects.all()
    alo = Alojamiento.objects.filter(destino__nombre=request.POST['destino'])
    despOrigen = Desplazamiento.objects.filter(origen__nombre=request.POST['origen'])
    despDestino = Desplazamiento.objects.filter(origen__nombre=request.POST['destino'])
    paq = Paquete.objects.filter(destino__nombre=request.POST['destino'])

    print(despOrigen, despDestino)

    context = {
        'destinos': dest,
        'alojamientos': alo,
        'desplazamientosOrigen': despOrigen,
        'desplazamientosDestino': despDestino,
        'paquetes': paq,
    }

    # Filtrar alojamientos segun destino:
    # Opción 1:
    #alojamiento = Alojamiento.objects.filter(destino__nombre=request.POST['destino'])

    # Opción 2:
    #destinoId = Destino.objects.filter(nombre=request.POST['destino'])
    #alojamiento = Alojamiento.objects.filter(destino=destinoId.id)

    #Filtrar desplazamientos por destino y origen:
    # desplazamientosIda = Desplazamiento.objects.filter(origen__nombre=request.POST['origen'], destino__nombre=request.POST['destino'])
    # desplazamientosVuelta = Desplazamiento.objects.filter(origen__nombre=request.POST['destino'], destino__nombre=request.POST['origen']) 

    # print (alojamiento, desplazamientosIda, desplazamientosVuelta)

    plantilla = loader.get_template('viaje_vista2.html')
    return HttpResponse(plantilla.render(context, request))