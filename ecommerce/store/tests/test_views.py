from unittest import skip
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product
from django.test import Client


@skip('demonstrating skipping')
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
