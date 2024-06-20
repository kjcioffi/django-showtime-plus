from typing import Any
from django.views.generic import TemplateView
from movies.exceptions import MovieApiException
from movies.movie_api_utils import MovieApiUtils

movie_utils = MovieApiUtils()


class MovieListView(TemplateView):
    context_object_name = "movies"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        try:
            movies = movie_utils.get_movies_now_playing()
            movies_with_date_objects = movie_utils.convert_date_string_into_object(
                movies, filter="results"
            )
            context["movies"] = movies_with_date_objects
        except MovieApiException as e:
            context["error_message"] = str(e)
        return context


class MovieDetailView(TemplateView):
    context_object_name = "movie"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        movie_id = kwargs["id"]
        movie = movie_utils.get_movie_details(movie_id)
        actors = movie_utils.get_movie_actors(movie_id)

        context["movie"] = movie
        context["actors"] = actors
        return context
