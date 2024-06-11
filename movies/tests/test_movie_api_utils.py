from django.test import TestCase
from requests import Response

from movies.exceptions import MovieApiException
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

    def test_movies_now_playing_fail(self):
        movie_api = MovieApiUtils()

        with self.assertRaises(MovieApiException):
            movie_api.api_key = ""
            movie_api.headers["Authorization"] = "Bearer ''"
            movie_api.get_movies_now_playing()

    def test_movies_now_playing_success(self):
        movies = self.movie_api_utils.get_movies_now_playing()
        self.assertIsInstance(movies, Response)
        self.assertTrue(movies.json()["results"])

        for movie in movies.json()["results"]:
            self.assertTrue(movie)
