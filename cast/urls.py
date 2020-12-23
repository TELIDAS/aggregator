from django.urls import path
from .views import CastView, CastDetailView, CharacterView, CharacterDetailView, TvActorView, TvActorDetailView

urlpatterns = [
    path('cast/', CastView.as_view()),
    path('cast/<int:pk>/', CastDetailView.as_view()),
    path('character/', CharacterView.as_view()),
    path('character/<int:pk>/', CharacterDetailView.as_view()),
    path('tvactor/', TvActorView.as_view()),
    path('tvactor/<int:pk>/', TvActorDetailView.as_view()),
]