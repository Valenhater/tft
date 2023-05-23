#from django.shortcuts import get_list_or_404, render
from .models import Paquete
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
   lc = Paquete.objects.all()
   context = {
        'paquetes': lc,
    }
   plantilla = loader.get_template('viaje_list.html')
   return HttpResponse(plantilla.render(context, request))

def vista2():
    pass