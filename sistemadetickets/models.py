"""
Este archivo define el modelo principal Ticket.
Permite almacenar y gestionar tickets de soporte.
Incluye campos basicos como titulo, descripcion y estado.
Relaciona cada ticket con usuarios de Django.
Usado por la API REST y el admin.
"""

from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('en_progreso', 'En progreso'),
        ('cerrado', 'Cerrado'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='abierto')
    creado_por = models.ForeignKey(User, related_name='tickets_creados', on_delete=models.CASCADE)
    asignado_a = models.ForeignKey(User, related_name='tickets_asignados', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.titulo)
