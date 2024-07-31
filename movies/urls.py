from django.urls import path

from movies.views import MovieListCreateView, MovieDetailUpdateDeleteView, MovieStatsView


urlpatterns = [

    path('movies/', MovieListCreateView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieDetailUpdateDeleteView.as_view(), name='movies-detail-update-delete-view'),
    path('movies/stats', MovieStatsView.as_view(), name='movie-stats')
]
