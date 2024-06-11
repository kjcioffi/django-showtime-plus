from django.utils import timezone
import datetime
import environ
import requests


class MovieApiUtils:
    """
    MovieApiUtils is a utility class for fetching information
    from the movie database (TMDB) api.

    https://developer.themoviedb.org/reference/intro/getting-started
    """

    env = environ.Env()

    AUTHENTICATE = "https://api.themoviedb.org/3/authentication"

    MOVIES_IN_THEATERS = (
        "https://api.themoviedb.org/3/discover/movie?"
        + "include_adult=true&"
        + "include_video=true&"
        + "language=en-US&"
        + "primary_release_date.gte={date}&"
        + "sort_by=popularity.desc"
    )

    API_KEY = env("TMDB_API_KEY", default="")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    def authenticate(self):
        return requests.get(self.AUTHENTICATE, headers=self.headers).json()

    def get_movies_now_playing(self):
        today = timezone.now().date()
        month_and_half_ago = today - datetime.timedelta(days=45)
        return requests.get(
            self.MOVIES_IN_THEATERS.format(date=month_and_half_ago.isoformat()),
            headers=self.headers,
        )
