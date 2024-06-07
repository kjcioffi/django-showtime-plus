from django.shortcuts import render
from movies.movie_api_utils import MovieApiUtils


def index(request):
    movie_utils = MovieApiUtils()
    movies = movie_utils.get_movies_now_playing().json()
    return render(request, "movies/index.html", {"movies": movies})
