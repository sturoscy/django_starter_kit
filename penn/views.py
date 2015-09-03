from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie

from penn.permissions import is_wharton_user
from penn.call_wisp_api import call_wisp_api

class EnsureCsrfToken(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(EnsureCsrfToken, cls).as_view(**initkwargs)
        return ensure_csrf_cookie(view)

class IsWhartonUser(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(IsWhartonUser, cls).as_view(**initkwargs)
        return is_wharton_user(view)

class IsWhartonHRUser(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(IsWhartonHRUser, cls).as_view(**initkwargs)
        return is_wharton_hr_user(view)

def penn_logout(request):
    logout(request)
    response = redirect('https://weblogin.pennkey.upenn.edu/logout')
    response.delete_cookie(request.META.get('COSIGN_SERVICE'))
    return response