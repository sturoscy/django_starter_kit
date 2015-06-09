from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ROLLBAR = {
    'access_token': 'YOUR_POST_SERVER_ITEM_ACCESS_TOKEN',
    'environment': 'production',
    'branch': 'master',
    'root': '/var/www/html/wisp',
}