#from django.shortcuts import get_list_or_404, render
from .models import viajes
#from django.http import HttpResponse
#from django.template import loader
#from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ViajesListView(ListView):
    model = Viajes
