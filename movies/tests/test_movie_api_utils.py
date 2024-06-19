from datetime import datetime
from django.test import TestCase

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

    def test_invalid_api_key(self):
        with self.assertRaises(MovieApiException):
            movie_api = MovieApiUtils()
            movie_api.api_key = ""
            movie_api.headers["Authorization"] = "Bearer ''"
            movie_api.get_movies_now_playing()

    def test_movies_now_playing_success(self):
        movies = self.movie_api_utils.get_movies_now_playing()
        self.assertIsInstance(movies, dict)
        self.assertTrue(movies["results"])

        for movie in movies["results"]:
            self.assertTrue(movie)

    def test_bad_json_in_date_conversion(self):
        movies = self.movie_api_utils.MOVIES_IN_THEATERS
        with self.assertRaisesMessage(
            MovieApiException, "Ensure JSON argument is a dictionary object."
        ):
            self.movie_api_utils.convert_date_string_into_object(
                movies, filter="results"
            )

    def test_bad_filter_value_in_date_conversion(self):
        movies = self.movie_api_utils.get_movies_now_playing()
        filter = "bad_filter"
        with self.assertRaisesMessage(
            MovieApiException, f"{filter} is not a valid attribute on a movie object."
        ):
            self.movie_api_utils.convert_date_string_into_object(movies, filter=filter)

    def test_successful_date_conversion(self):
        movies = self.movie_api_utils.get_movies_now_playing()

        for movie in movies["results"]:
            self.assertIsInstance(movie["release_date"], str)

        try:
            movies_with_dates = self.movie_api_utils.convert_date_string_into_object(
                movies, filter="results"
            )

            for movie in movies_with_dates["results"]:
                self.assertIsInstance(
                    movie["release_date"],
                    datetime,
                    "Movie release date should be a datetime object.",
                )
        except Exception as e:
            self.fail(
                f"An issue has occurred with validating movie date conversion: {e}"
            )
