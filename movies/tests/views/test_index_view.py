from django.test import Client, TestCase
from django.urls import reverse
import requests
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse("movies:index"))

        self.api_key = env("TMDB_API_KEY")
        self.requests = requests

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        self.movies = requests.get(
            "https://api.themoviedb.org/3/movie/now_playing", headers=headers
        )
