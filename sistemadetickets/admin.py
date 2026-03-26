"""
admin.py
Configuración del panel de administración para el modelo Ticket.
Permite gestionar los tickets desde el admin de Django.
"""

from django.contrib import admin
from .models import Ticket

# Configuración personalizada para mostrar y filtrar tickets en el admin
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estado', 'creado_por', 'asignado_a', 'fecha_creacion')  # Columnas visibles
    list_filter = ('estado', 'creado_por', 'asignado_a')  # Filtros laterales
    search_fields = ('titulo', 'descripcion')  # Búsqueda por título o descripción
