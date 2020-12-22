from django.contrib import admin

# Register your models here.
from .models import Cast, Characters, TvActor

admin.site.register(Cast)
admin.site.register(Characters)
admin.site.register(TvActor)