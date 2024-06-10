from typing import Any
from django.views.generic import TemplateView
from movies.movie_api_utils import MovieApiUtils

movie_utils = MovieApiUtils()


class MovieListView(TemplateView):
    context_object_name = "movies"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["movies"] = movie_utils.get_movies_now_playing().json()
        return context
