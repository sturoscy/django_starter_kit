from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

INSTALLED_APPS = INSTALLED_APPS + ('rollbar',)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('rollbar.contrib.django.middleware.RollbarNotifierMiddleware',)

ROLLBAR = {
    'access_token': 'YOUR_POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'production',
    'branch': 'master',
    'root': '/var/www/html/wisp',
}