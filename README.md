# Sistema de Gestión de Tickets (Django REST)

Este proyecto es una API REST para la gestión de tickets de soporte, desarrollada con Django, Django REST Framework y autenticación JWT. Incluye comentarios y nombres en español para facilitar su comprensión.

## Características principales
- Gestión de tickets: crear, listar, actualizar y eliminar tickets.
- Autenticación JWT (JSON Web Token).
- Serialización de usuarios y tickets.
- Panel de administración de Django para gestión manual.
- Código y comentarios en español.

## Requisitos previos
- Python 3.8+
- pip
- (Recomendado) Entorno virtual: venv

## Instalación

1. **Clona el repositorio o copia los archivos en tu máquina.**

2. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Mac/Linux:
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```sh
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. **Realiza las migraciones:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un superusuario para el panel de administración:**
   ```sh
   python manage.py createsuperuser
   ```

6. **Inicia el servidor de desarrollo:**
   ```sh
   python manage.py runserver
   ```

## Uso

- Accede al panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Endpoints de la API:
  - Obtener token JWT: `POST /api/token/` (usuario y contraseña)
  - Refrescar token: `POST /api/token/refresh/`
  - CRUD de tickets: `/api/tickets/`

### Ejemplo de autenticación y uso con `curl`

1. **Obtener token:**
   ```sh
   curl -X POST -d "username=TU_USUARIO&password=TU_CONTRASEÑA" http://127.0.0.1:8000/api/token/
   ```
   Respuesta:
   ```json
   { "access": "TOKEN", "refresh": "TOKEN" }
   ```

2. **Listar tickets:**
   ```sh
   curl -H "Authorization: Bearer TU_TOKEN" http://127.0.0.1:8000/api/tickets/
   ```

3. **Crear un ticket:**
   ```sh
   curl -X POST -H "Authorization: Bearer TU_TOKEN" -H "Content-Type: application/json" \
        -d '{"titulo": "Error en login", "descripcion": "No puedo acceder", "estado": "abierto"}' \
        http://127.0.0.1:8000/api/tickets/
   ```

## Estructura del proyecto

- `sistemadetickets/` — Configuración principal de Django
- `tickets/` — App principal con modelos, vistas, serializadores y rutas

## Personalización
- Puedes modificar los modelos, permisos y vistas según tus necesidades.
- Para agregar roles diferenciados, consulta la documentación de Django y DRF sobre permisos personalizados.

## Licencia
Este proyecto es de uso educativo y libre.
