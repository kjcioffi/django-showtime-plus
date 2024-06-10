from django.utils import timezone
import datetime
import environ
import requests


class MovieApiUtils:
    env = environ.Env()

    MOVIES_IN_THEATERS = (
        "https://api.themoviedb.org/3/discover/movie?" +
        "include_adult=false&" +
        "include_video=false&" +
        "language=en-US&" +
        "page=1&" +
        "primary_release_date.gte={date}&" +
        "sort_by=popularity.desc"
    )

    API_KEY = env("TMDB_API_KEY", default="")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    def get_movies_now_playing(self):
        today = timezone.now().date()
        month_and_half_ago = today - datetime.timedelta(days=45)
        return requests.get(
            self.MOVIES_IN_THEATERS.format(date=month_and_half_ago.isoformat()),
            headers=self.headers,
        )
