from django.test import TestCase

from movies.movie_api_utils import MovieApiUtils


class TestMovieApiUtils(TestCase):
    def setUp(self):
        self.movie_api_utils = MovieApiUtils()

    def test_valid_api_key(self):
        response = self.movie_api_utils.authenticate()
        self.assertNotEqual(
            response["status_message"],
            "Invalid API key: You must be granted a valid key.",
            "Ensure your TMDB API key is valid and functioning properly.",
        )
        self.assertEqual(response["success"], True)
