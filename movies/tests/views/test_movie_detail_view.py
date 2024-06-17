from django.test import TestCase

from django.urls import reverse

from movies.movie_api_utils import MovieApiUtils


class TestMovieDetailView(TestCase):
    def setUp(self):
        self.movie_api_utils = MovieApiUtils()
        self.movie_id = 653346
        self.view = self.client.get(reverse("movies:detail", kwargs={"id": self.movie_id}))

    def test_movie_in_context(self):
        movie = self.view.context["movie"]
        self.assertIsInstance(movie, dict)

    def test_movie_accurately_retrieved(self):
        movie = self.movie_api_utils.get_movie_details(self.movie_id)
        self.assertEqual(movie, self.view.context['movie'])
