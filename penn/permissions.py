from functools import wraps

from django.conf import settings
from django.core.exceptions import PermissionDenied

from penn.call_wisp_api import call_wisp_api

def is_wharton_user(view_func):
  @wraps(view_func)
  def wrapper(request, *args, **kwargs):
    if request.META.get('REMOTE_USER') is not None:
      url = 'https://apps.wharton.upenn.edu/wisp/api/v1/adgroups/%s' % request.META.get('REMOTE_USER')
      response = call_wisp_api(url)
      if 'STAFF' in response.get('groups'):
        return view_func(request, *args, **kwargs)
      else:
        raise PermissionDenied
    else:
      raise PermissionDenied
  return wrapper
  
def is_wharton_hr_user(view_func):
  @wraps(view_func)
  def wrapper(request, *args, **kwargs):
    if request.META.get('REMOTE_USER') is not None:
      url = 'https://apps.wharton.upenn.edu/wisp/api/v1/adgroups/%s' % request.META.get('REMOTE_USER')
      response = call_wisp_api(url)
      if 'Admin - HR - Staff - Administration' in response.get('groups'):
        return view_func(request, *args, **kwargs)
      else:
        raise PermissionDenied
    else:
      raise PermissionDenied
  return wrapper
