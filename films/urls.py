from django.urls import path
from .views import FilmView, AnimeView, TvShowView, FilmDetailView, AnimeDetailView, TvShowDetailView

urlpatterns = [
    path('films/', FilmView.as_view()),
    path('films/<int:pk>/', FilmDetailView.as_view()),
    path('anime/', AnimeView.as_view()),
    path('anime/<int:pk>/', AnimeDetailView.as_view()),
    path('shows/', TvShowView.as_view()),
    path('shows/<int:pk>/', TvShowDetailView.as_view()),

]
