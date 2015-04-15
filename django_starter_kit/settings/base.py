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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Import logging.py file

from .logging import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't!va3s+a$jnxeg*_^@l)!e!nk6nl*e2s%bl%tl6a+rx)kqvq=0'

ALLOWED_HOSTS = []

# Define Admins Contacts
ADMINS = (
    ('user_name', 'admin_email@address.net'),
)
MANAGERS = ADMINS


# Application definition
INSTALLED_APPS = (
    'compressor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
    'bootstrap3',
    'base_theme',
    'rest_framework',
    'rollbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
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

# Static Files

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_dev"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Tell Django where to find templates.

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Bower assets

BOWER_COMPONENTS_ROOT = '/django_starter_kit/static_dev/bower_components/'

# BOWER_INSTALLED_APPS should be in sync with bower.json at project root
BOWER_INSTALLED_APPS = (
    'jquery-ui#1.11.4',
    'underscore#1.8.2',
    'backbone#1.1.2',
    'q#1.0.1',
)
