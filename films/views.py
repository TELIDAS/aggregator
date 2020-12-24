from django.views.decorators.csrf import csrf_exempt

from films.forms import CommentForm
from films.models import Film, Anime, TvShow
from django.views.generic import ListView, DetailView


class FilmView(ListView):
    template_name = 'films/film_index.html'

    def get_queryset(self):
        return Film.objects.all()


class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/films_detail.html'
    extra_context = {'form': CommentForm()}

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        film_id = kwargs['pk']
        film = Film.objects.get(pk=film_id)
        form = CommentForm(request.POST, initial={'film': film})
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)

class AnimeView(ListView):
    template_name = 'films/anime_index.html'

    def get_queryset(self):
        return Anime.objects.all()

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'films/anime_detail.html'
    extra_context = {'form': CommentForm()}

    @csrf_exempt
    def post(self, request, pk, *args, **kwargs):
        anime = Anime.objects.get(pk=pk)
        form = CommentForm(request.POST, initial={'anime': anime})
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)

class TvShowView(ListView):
    template_name = 'films/show_index.html'

    def get_queryset(self):
        return TvShow.objects.all()

class TvShowDetailView(DetailView):
    model = TvShow
    template_name = 'films/show_detail.html'
    extra_context = {'form': CommentForm()}

    @csrf_exempt
    def post(self, request, pk, *args, **kwargs):
        shows = TvShow.objects.get(pk=pk)
        form = CommentForm(request.POST, initial={'shows': shows})
        if form.is_valid():
            form.save()

        return self.get(request, *args, **kwargs)
