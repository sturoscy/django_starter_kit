from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_starter_kit.views import BaseView, MockView

urlpatterns = patterns('',
	url(r'^', BaseView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'mock/', MockView.mock),
)
