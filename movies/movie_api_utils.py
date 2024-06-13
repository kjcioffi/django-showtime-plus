from django.utils import timezone
import datetime
import environ
import requests

from movies.exceptions import MovieApiException


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

    def __init__(self):
        self.api_key = self.env("TMDB_API_KEY", default="")

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

    def authenticate(self):
    def get_movies_now_playing(self):
        today = timezone.now().date()
        month_and_half_ago = today - datetime.timedelta(days=45)
        url = self.MOVIES_IN_THEATERS.format(date=month_and_half_ago.isoformat())
        return self._get(url=url)

    def _get(self, url, **kwargs) -> dict[str, str]:
        """
        A wrapper class for performing HTTP get requests via the requests library.
        """
        try:
            response: requests.Response = requests.get(
                url=url, params=kwargs, headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise MovieApiException("Failed to retrieve data from the movie database.")
        except requests.exceptions.ConnectionError:
            raise MovieApiException(
                "Network connection error occurred while accessing the movie database."
            )
        except requests.exceptions.Timeout:
            raise MovieApiException("Request to the movie database timed out.")
        except requests.exceptions.RequestException:
            raise MovieApiException("An error occurred while processing your request.")
