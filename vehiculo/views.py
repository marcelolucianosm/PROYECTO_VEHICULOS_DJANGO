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
    
class VehiculoAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name = "vehiculos/add_vehiculo.html"
    fields = ['marca', 'modelo','serial_carroceria','serial_motor','categoria','precio','fecha_creacion','fecha_modificacion']
    success_url = reverse_lazy('vehiculo')
    permission_required = 'vehiculo.add_vehiculo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Nivel de acceso Prohibido para acceder a la vista.")
            return redirect("index")
        
        else:
            messages.info(self.request, "Debe iniciar sesión para continuar.")
            return redirect("login")
