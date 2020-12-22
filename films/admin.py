from django.contrib import admin

# Register your models here.
from .models import Film, TvShow, Anime

admin.site.register(Film)
admin.site.register(TvShow)
admin.site.register(Anime)
