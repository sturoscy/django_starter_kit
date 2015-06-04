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

    def test_page(self):
        response = self.client.get('/test', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_page_output_message(self):
        response = self.client.get('/test', follow=True)
        self.assertIn('Output: But did your test pass?', response.content.decode())

    # This test is incomplete and the rest of the application does
    # not have anything to help you with this. Try to figure it out!
    def test_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'

        response = self.client.get('/test', follow=True)

        self.assertEqual(response.status_code, 302)
