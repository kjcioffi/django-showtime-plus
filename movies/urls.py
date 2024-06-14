from django.urls import path
import movies.views as views

app_name = "movies"
urlpatterns = [
    path(
        "",
        views.MovieListView.as_view(template_name="movies/movie_list.html"),
        name="index",
    ),
    path(
        "movie/<int:id>",
        views.MovieDetailView.as_view(template_name="movies/movie_detail.html"),
        name="detail",
    ),
]
