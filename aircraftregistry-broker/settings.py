"""
Django settings for aircraftregistry-broker project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku
from dotenv import load_dotenv, find_dotenv
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^z_a@yyzuplya(g*9!9gn2s^jl-&c&i_ulqm8m*5qkx9q0@_k-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'social_django',
    'rest_framework',
    'auth0authorization',
    'switchboard'
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


AUTHENTICATION_BACKENDS = {
    'auth0authorization.auth0backend.Auth0',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/search'

ROOT_URLCONF = 'aircraftregistry-broker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'aircraftregistry-broker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'switchboard.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

SOCIAL_AUTH_TRAILING_SLASH = False
if DEBUG:
    ENV_FILE = find_dotenv()
    if ENV_FILE:
        load_dotenv(ENV_FILE)

SOCIAL_AUTH_AUTH0_KEY = os.environ.get('AUTH0_CLIENT_ID')
SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')

SOCIAL_AUTH_AUTH0_SCOPE = [
        "registry.read.operator",
        "registry.read.address",
        "registry.read.person",
        "registry.read.contact",
        "registry.read.pilot",
        "registry.read.aircraft",
        "registry.read.authorization",
        "registry.read.activity",
        "registry.read.address.privileged",
        "registry.read.aircraft.privileged",
        "registry.read.operator.privileged",
        "registry.read.contact.privileged",
        "registry.read.pilot.privileged",
      
]
SOCIAL_AUTH_AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
AUDIENCE = None


if os.environ.get('AUTH0_AUDIENCE'):
    AUDIENCE = os.environ.get('AUTH0_AUDIENCE')
else:
    if SOCIAL_AUTH_AUTH0_DOMAIN:
        AUDIENCE = 'https://' + SOCIAL_AUTH_AUTH0_DOMAIN + '/userinfo'
if AUDIENCE:
    SOCIAL_AUTH_AUTH0_AUTH_EXTRA_ARGUMENTS = {'audience': AUDIENCE}


if DEBUG:
    BROKER_URL = 'redis://localhost:6379/'
else:
    BROKER_URL = os.environ.get("REDIS_URL")
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
django_heroku.settings(locals())