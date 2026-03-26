"""
Este archivo configura ASGI para el proyecto.
Permite desplegar la aplicacion en servidores ASGI.
Expone la variable application para el servidor.
Carga la configuracion de Django.
No requiere modificaciones para uso comun.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemadetickets.settings')

application = get_asgi_application()
