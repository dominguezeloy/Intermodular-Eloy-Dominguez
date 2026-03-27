"""
Este archivo contiene los serializadores de la API.
Convierte modelos a JSON y viceversa.
Incluye serializador de usuario y de ticket.
Permite validar y estructurar los datos de la API.
Es usado por las vistas de la API REST.
"""

from rest_framework import serializers
from .models import Ticket
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:  # type: ignore
        model = User
        fields = ['id', 'username', 'email']

class TicketSerializer(serializers.ModelSerializer):  # type: ignore
    creado_por = UsuarioSerializer(read_only=True)
    asignado_a = UsuarioSerializer(read_only=True)

    class Meta:  # type: ignore
        model = Ticket
        fields = '__all__'
