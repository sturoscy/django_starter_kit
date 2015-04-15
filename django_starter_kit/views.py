from django.shortcuts import render
from django.views.generic import TemplateView
import logging, os, rollbar

rollbar.init('39b8de9527484878a2432949aef3dd0f', 'develop-test')

try:
  main_app_loop()
except IOError:
  rollbar.report_message('Got an IOError in the main loop', 'error')
except:
  rollbar.report_exc_info()

# BaseView
class BaseView(TemplateView):
    template_name = 'starter_kit_base.html'
