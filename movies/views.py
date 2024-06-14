from typing import Any
from django.http import HttpResponse
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
            context["movies"] = movies
        except MovieApiException as e:
            context["error_message"] = str(e)
        return context


def movie_detail(request, id):
    return HttpResponse(id)
