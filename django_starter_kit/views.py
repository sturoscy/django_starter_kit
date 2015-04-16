from django.shortcuts import render
from django.views.generic import TemplateView

import os

# BaseView
class BaseView(TemplateView):
    template_name = 'starter_kit_base.html'
