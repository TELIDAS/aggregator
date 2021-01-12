from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from films.forms import CommentForm, ParserForm
from films.models import Film, Anime, TvShow
from django.views.generic import ListView, DetailView, FormView


class FilmView(ListView):
    template_name = 'films/film_index.html'

    def get_queryset(self):
        return Film.objects.all()


class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/films_detail.html'
    extra_context = {'form': CommentForm()}


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated and self.object.age_limit <= request.user.age:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request=request, template_name='films/error_template.html')


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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


class ParserAnimeView(FormView):
    template_name = 'parser_form.html'
    form_class = ParserForm
    success_url = '/anime/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)


class ParserShowsView(ParserAnimeView, FormView):
    template_name = 'parser_form.html'
    form_class = ParserForm
    success_url = '/shows/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserShowsView, self).post(request, *args, **kwargs)
