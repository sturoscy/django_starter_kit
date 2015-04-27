from .base import *

# Turn on DEBUG and TEMPLATE_DEBUG, but only in dev; these are set to False in base.py, and overridden here.

DEBUG = True
TEMPLATE_DEBUG = True

# Set up your static paths - maybe just keep this in base?

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Allows show Django debug toolbar in dev.

def custom_show_toolbar(self):
    return True

DEBUG_TOOLBAR_PATCH_SETTINGS = True

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'django_starter_kit.settings.dev.custom_show_toolbar',
}

INTERNAL_IPS = ('127.0.0.1', '128.91.*.*',)

# Dev Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

ROLLBAR = {
    'access_token': '39b8de9527484878a2432949aef3dd0f',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/vagrant/python-dev/html/django_starter_kit',
}