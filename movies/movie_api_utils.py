from typing import Any
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

    MOVIE_DETAILS = "https://api.themoviedb.org/3/movie/{movie_id}"

    def __init__(self):
        self.api_key = self.env("TMDB_API_KEY", default="")

        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        self.authenticated = self.authenticate()

    def authenticate(self) -> dict[str, Any]:
        """
        Checks if authentication with the TMDB API was valid.
        """
        try:
            return self._get(url=self.AUTHENTICATE)
        except requests.exceptions.RequestException:
            raise MovieApiException("Failed to authenticate with movie database API.")

    def get_movies_now_playing(self) -> dict[str, Any]:
        """
        Retrieves movies released in the past 45 days.
        """
        today = timezone.now().date()
        month_and_half_ago = today - datetime.timedelta(days=45)
        url = self.MOVIES_IN_THEATERS.format(date=month_and_half_ago.isoformat())
        return self._get(url=url)

    def get_movie_details(self, movie_id) -> dict[str, Any]:
        """
        Retrieves the details of a movie by it's ID.
        """
        url = self.MOVIE_DETAILS.format(movie_id=movie_id)
        return self._get(url=url)

    def _get(self, url, **kwargs) -> dict[str, Any]:
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

    def convert_date_string_into_object(
        self, movies, *, filter: str = None
    ) -> dict[str, Any]:
        """
        Iterates through a collection of movies and converts their release date string into a datetime object.

        :param json movies: The API response received.
        :param str filter: Represents a key in the JSON payload that contains movie data, in case the data is nested under this key. \
            Hence, you need to know which key contains the movie data in the JSON payload.
        """
        try:
            movies_to_process = movies if filter is None else movies[filter]

            for movie in movies_to_process:
                movie["release_date"] = datetime.datetime.strptime(
                    movie["release_date"], "%Y-%m-%d"
                )

            return movies
        except TypeError:
            raise MovieApiException("Ensure JSON argument is a dictionary object.")
        except KeyError:
            raise MovieApiException(
                f"{filter} is not a valid attribute on a movie object."
            )
