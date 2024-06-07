from django.test import Client, TestCase
from django.urls import reverse
from requests import Response


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("movies:index"))

    def test_movies_in_context(self):
        view = self.client.get(reverse("movies:index"))
        movies_in_context = view.context["movies"]
        self.assertTrue(movies_in_context)
        self.assertIsInstance(movies_in_context, Response)
