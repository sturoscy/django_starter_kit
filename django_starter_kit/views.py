from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import os

# BaseView
class BaseView(TemplateView):
    template_name = 'starter_kit_base.html'

# MockView
class TestView(object):

    def test(request):
        message = 'But did your test pass?'
        return render(request, 'test_view/test_view_page.html', { 'message': message })
