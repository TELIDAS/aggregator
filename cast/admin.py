from django.contrib import admin

# Register your models here.
from .models import Cast, Character, TvActor

admin.site.register(Cast)
admin.site.register(Character)
admin.site.register(TvActor)