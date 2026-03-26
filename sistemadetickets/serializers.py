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

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TicketSerializer(serializers.ModelSerializer):
    creado_por = UsuarioSerializer(read_only=True)
    asignado_a = UsuarioSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
