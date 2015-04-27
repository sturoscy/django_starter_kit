from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django_starter_kit.views import BaseView
# Unittests for Django starter kit.


class HomePageTest(TestCase):

    def test_root_url_renders_template_starter_kit_base(self):
        response = self.client.get('', follow=True)
        expected_html = render_to_string('starter_kit_base.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_root_url_resolves_to_200(self):
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)


        
    # def setUp(self):
    #     # Every test needs a client.
    #     self.client = Client()

    # def test_details(self):
    #     # Issue a GET request.
    #     response = self.client.get('/customer/details/')

    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)

    #     # Check that the rendered context contains 5 customers.
    #     self.assertEqual(len(response.context['customers']), 5)