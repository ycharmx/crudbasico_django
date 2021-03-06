"""
Django settings for crudbasico project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Instancia de la clase LoadConfig
from .base import LoadConfig
configuracion = LoadConfig('apps_config.json')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = configuracion.get_env_var('email')
EMAIL_HOST_PASSWORD = configuracion.get_env_var('email_password')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hp4+30cj--2i$9ce4i48%q-fassuwx00w8xm18pmz5%&5ar$h2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = configuracion.get_env_var('debug')

ALLOWED_HOSTS = [configuracion.get_env_var('allowed_host')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'bootstrap_datepicker_plus',
    'apps.crud',
    'apps.render_pdf',
    'apps.email_exceptions',
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

ROOT_URLCONF = 'crudbasico.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #Agregando los directorios de los templates ==> crud
            BASE_DIR + '/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ID_ENCRYPT_KEY = 'XUN1Ws76qR0w_9qKcTMRQ6ObR8rhDPgV5beZmmNeZCk='

WSGI_APPLICATION = 'crudbasico.wsgi.application'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'static/css'),
    os.path.join(BASE_DIR,'static/js'),
    os.path.join(BASE_DIR,'static/bootstrap_datepicker_plus')
]

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': configuracion.get_env_var('sqlserver_database'),
        'USER': configuracion.get_env_var('sqlserver_user'),
        'PASSWORD': configuracion.get_env_var('sqlserver_password'),
        'HOST': configuracion.get_env_var('sqlserver_host'),
        'PORT': '',
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

#cambiamos el lenguaje a español mexico
LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
