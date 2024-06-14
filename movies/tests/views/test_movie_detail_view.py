from django.test import TestCase

from django.urls import reverse

from movies.movie_api_utils import MovieApiUtils


class TestMovieDetailView(TestCase):
    def setUp(self):
        self.movie_api_utils = MovieApiUtils()
        self.view = self.client.get(reverse("movies:detail", kwargs={"id": 653346}))
