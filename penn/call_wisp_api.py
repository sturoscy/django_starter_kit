from django.conf import settings

import requests

def call_wisp_api(url=None, params=None):
  headers = { 'Authorization': 'Token %s' % settings.WISP_TOKEN }
  response = requests.get(url, headers=headers, params=params).json()
  return response
