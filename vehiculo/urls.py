from django.urls import path
from . import views

urlpatterns = [
    path('vehiculo/', views.VehiculosView.as_view(), name='vehiculo'),

]