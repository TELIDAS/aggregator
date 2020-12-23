


from films.models import Film, Anime, TvShow
from django.views.generic import ListView, DetailView


class FilmView(ListView):
    template_name = 'films/film_index.html'

    def get_queryset(self):
        return Film.objects.all()


class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/films_detail.html'

class AnimeView(ListView):
    template_name = 'films/anime_index.html'

    def get_queryset(self):
        return Anime.objects.all()

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'films/anime_detail.html'

class TvShowView(ListView):
    template_name = 'films/show_index.html'

    def get_queryset(self):
        return TvShow.objects.all()

class TvShowDetailView(DetailView):
    model = TvShow
    template_name = 'films/show_detail.html'