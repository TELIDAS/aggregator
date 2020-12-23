from django.views.generic import ListView, DetailView

from cast.models import Characters, Cast, TvActor

class CastView(ListView):
    template_name = 'cast/cast_index.html'

    def get_queryset(self):
        return Cast.objects.all()
class CastDetailView(DetailView):
    model = Cast
    template_name = 'cast/cast_detail.html'


class CharacterView(ListView):
    template_name = 'cast/character_index.html'

    def get_queryset(self):
        return Characters.objects.all()
class CharacterDetailView(DetailView):
    model = Characters
    template_name = 'cast/characters_detail.html'


class TvActorView(ListView):
    template_name = 'cast/tvactor_index.html'

    def get_queryset(self):
        return TvActor.objects.all()
class TvActorDetailView(DetailView):
    model = TvActor
    template_name = 'cast/tvactor_detail.html'