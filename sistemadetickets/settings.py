"""
Este archivo contiene la configuracion principal del proyecto.
Define apps instaladas, base de datos y rutas estaticas.
Incluye configuracion de seguridad y lenguaje.
Se usa para ajustar el comportamiento de Django.
Es el corazon de la configuracion del proyecto.
"""

from pathlib import Path

 # Construye rutas dentro del proyecto como BASE_DIR / 'subcarpeta'.
BASE_DIR = Path(__file__).resolve().parent.parent


 # Configuracion rapida para desarrollo - no usar en produccion
 # Ver https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

 # ADVERTENCIA: mantenga la clave secreta en privado en produccion
SECRET_KEY = 'django-insecure-*@q6=dgm-j!@=1u4j4uzj*7nqeu_&5f**k)bwj$bozgxb&78o)'

 # ADVERTENCIA: no active debug en produccion
DEBUG = True

ALLOWED_HOSTS = []


 # Definicion de aplicaciones instaladas

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sistemadetickets',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sistemadetickets.urls'

from typing import Any

TEMPLATES: list[dict[str, Any]] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sistemadetickets.wsgi.application'


 # Base de datos
 # Ver https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES: dict[str, dict[str, Any]] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


 # Validacion de passwords
 # Ver https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


 # Internacionalizacion
 # Ver https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


 # Archivos estaticos (CSS, JavaScript, Imagenes)
 # Ver https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

 # Configuracion de Django REST Framework y JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

from datetime import timedelta
SIMPLE_JWT: dict[str, Any] = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
