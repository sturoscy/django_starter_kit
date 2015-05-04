from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


import os


# BaseView
class BaseView(TemplateView):
    template_name = 'starter_kit_base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['rollbar_access_token'] = settings.ROLLBAR.get('access_token')
        return context


# MockView
class MockView():

    def mock(request):
        message = 'But did your test pass?'
        return render(request, 'MockView/mock_view_page.html', {'message': message})
