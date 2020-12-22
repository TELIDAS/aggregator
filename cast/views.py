from django.shortcuts import render


# Create your views here.
from django.views.generic.base import View

from cast.models import Characters


class CharactersView(View):
    model = Characters