"""
Este archivo define las vistas de la API REST.
Incluye el ViewSet principal para tickets.
Gestiona operaciones CRUD sobre tickets.
Requiere autenticacion JWT para acceder.
Usa los serializadores y modelos definidos.
"""

from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class TicketViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Ticket.objects.all().order_by('-fecha_creacion')
    serializer_class = TicketSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):  # type: ignore
        serializer.save(creado_por=self.request.user)
