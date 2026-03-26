"""
Este archivo configura la app principal de Django.
Define el nombre y el tipo de campo auto para IDs.
Es necesario para registrar la app en settings.py.
No requiere cambios para uso comun.
Se usa en proyectos Django modernos.
"""

from django.apps import AppConfig

class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sistemadetickets'
