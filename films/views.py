from django.shortcuts import render

# Create your views here.


# Create your views here.
from django.views.generic.base import View

from films.models import Anime


class AnimeView(View):
    model = Anime
