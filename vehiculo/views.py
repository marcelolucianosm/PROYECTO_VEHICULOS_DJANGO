from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

from .models import Vehiculo

class VehiculosView(ListView):
    model = Vehiculo
    template_name = "vehiculos/vehiculos.html"
    context_object_name = 'vehiculos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Página de Vehiculos'
        return context
