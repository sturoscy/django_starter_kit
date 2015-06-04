from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import os

# BaseView
class BaseView(TemplateView):
    template_name = 'starter_kit_base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['rollbar_access_token'] = settings.ROLLBAR.get('access_token')
        return context

# MockView
class TestView(object):

    def test(request):
        message = 'But did your test pass?'
        return render(request, 'test_view/test_view_page.html', { 'message': message })
