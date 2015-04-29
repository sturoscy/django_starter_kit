from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django_starter_kit.views import BaseView
# Unittests for Django starter kit.


class StarterKitTests(TestCase):


    def test_root_url_resolves_to_200(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_mock_page(self):
        response = self.client.get('/mock', follow=True)
        self.assertEqual(response.status_code, 200)
