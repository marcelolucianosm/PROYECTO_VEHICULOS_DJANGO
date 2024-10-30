from django.contrib import admin
from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['marca', 'modelo','serial_carroceria','serial_motor','categoria','precio','fecha_creacion','fecha_modificacion']
    list_display = ['marca', 'modelo','serial_carroceria','serial_motor','categoria','precio','fecha_creacion','fecha_modificacion']
    ordering = ['marca']
    list_filter = ['marca']
