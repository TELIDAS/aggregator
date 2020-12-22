from django.urls import path
from .views import CharactersView

urlpatterns = [
    path('characters/', CharactersView.as_view()),
]
