from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend

from penn.call_wisp_api import call_wisp_api

class PennRemoteUserBackend(RemoteUserBackend):
    def configure_user(self, user):
        response    = call_wisp_api('https://apps.wharton.upenn.edu/wisp/api/v1/adusers', { 'username': user.username })
        results     = response['results'][0]

        user.first_name = results['first_name']
        user.last_name  = results['last_name']
        user.email      = results['email'].replace('exchange.', '')
        user.is_staff   = True
        user.save()
