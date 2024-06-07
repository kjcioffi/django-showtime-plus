from django.test import Client, TestCase
from django.urls import reverse
from requests import Response


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("movies:index"))
        self.movies_in_context = self.response.context["movies"]

    def test_movies_in_context(self):
        self.assertTrue(self.movies_in_context)
        self.assertIsInstance(self.movies_in_context, dict)

