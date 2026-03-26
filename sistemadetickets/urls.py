"""
Este archivo define las rutas principales del proyecto.
Incluye rutas para el panel de administracion y la API REST.
Configura rutas para autenticacion JWT.
Registra las rutas del ViewSet de tickets.
Es el punto de entrada para las URLs de Django.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet


from django.urls import URLPattern, URLResolver

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
