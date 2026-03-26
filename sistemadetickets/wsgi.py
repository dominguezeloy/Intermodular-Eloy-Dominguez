"""
Este archivo configura WSGI para el proyecto.
Permite desplegar la aplicacion en servidores WSGI.
Expone la variable application para el servidor.
Carga la configuracion de Django.
No requiere modificaciones para uso comun.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemadetickets.settings')

application = get_wsgi_application()
