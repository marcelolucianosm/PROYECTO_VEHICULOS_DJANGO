from django.db import models

class Vehiculo(models.Model):
    class Meta:
        permissions = (('visualizar_catalogo', 'Ver Catalogo Vehiculos'),
                    ('add_vehiculomodel', 'Agregar Vehiculo'),)
    MARCAS = [
        ('CHEVROLET', 'CHEVROLET'),
        ('FIAT', 'FIAT'),
        ('FORD ', 'FORD'),
        ('TOYOTA', 'TOYOTA'),
    ]
    CATEGORIAS = [
        ('PARTICULAR', 'PARTICULAR'),
        ('TRANSPORTE', 'TRANSPORTE'),
        ('CARGA', 'CARGA'),
    ]
    
    marca = models.CharField(max_length=20, blank=False, null=False, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100, blank=False, null=False)
    serial_carroceria = models.CharField(max_length=50, blank=False, null=False)
    serial_motor = models.CharField(max_length=50, blank=False, null=False)
    categoria = models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIAS, default='Particular')
    precio = models.PositiveIntegerField(blank=False, null=False,)
    fecha_creacion = models.DateTimeField(blank=False, null=False)
    fecha_modificacion = models.DateTimeField(blank=False, null=False)

    
    def __str__(self) -> str:
        return self.marca
