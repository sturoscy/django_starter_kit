from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment if you are using Penn SSO
# from penn.views import penn_logout

from django_starter_kit.views import BaseView, TestView

urlpatterns = patterns('',
  url(r'^$', BaseView.as_view(), name='home'),
  # Uncomment if you are using Penn SSO
  # url(r'^logout/', penn_logout, name='penn-logout'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^test/', TestView.test),
)
