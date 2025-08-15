from django.db import models
from django.utils import timezone
from categorias.models import Item
from django.utils import timezone  # nuevo para fecha

class Peticion(models.Model):

    estado_peticion = [
        ("PENDIENTE", "Pendiente"),
        ("ACEPTADO", "Aceptado"),
        ("RECHAZADO", "Rechazado")
    ]

    titulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=Item.TIPO_CHOICES)
    autor = models.CharField(max_length=100, null=True, blank=True)
    estudio = models.CharField(max_length=100, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    editorial = models.CharField(max_length=100, null=True, blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    imagen = models.URLField(blank=True)


    #usuario = 
    estado = models.CharField(max_length=20, choices=estado_peticion, default="PENDIENTE")
    fecha_peticion = models.DateField(default=timezone.now) # nuevo fecha
    comentario_admin = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.titulo  # name to be shown when called
# Create your models here.
