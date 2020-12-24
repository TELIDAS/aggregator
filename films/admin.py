from django.contrib import admin

# Register your models here.
from .models import Film, TvShow, Anime, Comment

admin.site.register(Film)
admin.site.register(TvShow)
admin.site.register(Anime)
admin.site.register(Comment)
