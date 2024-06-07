from django.test import Client, TestCase
from django.urls import reverse
from movies.movie_api_utils import MovieApiUtils


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("movies:index"))

        self.movies_util = MovieApiUtils()

    def test_movies_in_context(self):
        view = self.client.get(reverse("movies:index"))
        movies_in_context = view.context["movies"]
        self.assertTrue(movies_in_context)
