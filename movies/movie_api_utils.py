import environ
import requests


class MovieApiUtils:
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    MOVIES_IN_THEATERS = "https://api.themoviedb.org/3/movie/now_playing"

    API_KEY = env("TMDB_API_KEY")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    def get_movies_now_playing(self):
        return requests.get(self.MOVIES_IN_THEATERS, headers=self.headers)
