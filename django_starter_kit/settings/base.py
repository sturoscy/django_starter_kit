"""
Django settings for django_starter_kit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
exit
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'YOUR_SECRET_KEY'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'fontawesome',
    'base_theme',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'django_starter_kit.urls'

WSGI_APPLICATION = 'django_starter_kit.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # Example for connecting to mssql (using moonwalker and WISP)
    # Update with your or your department's credentials
    'wisp': {
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'moonwalker.wharton.upenn.edu',
        'PORT': '1433',
        'NAME': 'wisp',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS': {
            'driver': 'FreeTDS',
            'host_is_server': True,
            'autocommit': True,
            ''
            'extra_params': 'TDS_VERSION=7.2'
        }
    },
}

# Caching

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'instruction_cache',
    }
}

# REST FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 50,
    'PAGINATE_BY_PARAM': 'page_size'
}


# Templates

# Tell Django where to find templates.

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
]


# Static Files

FONTAWESOME_CSS_URL = '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'

# Remove FileSystemFinder from STATICFILES_FINDERS
# if you are going to use gulpjs (http://gulpjs.com/)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_URL = '/django_starter_kit/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_dev"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Additional non-django settings

WISP_TOKEN = 'YOUR_WISP_TOKEN'
