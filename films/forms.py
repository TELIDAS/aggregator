from django import forms

from films.models import Comment, Film, Anime, TvShow


class CommentForm(forms.ModelForm):
    film = forms.ModelChoiceField(disabled=True, required=False, queryset=Film.objects.all())
    anime = forms.ModelChoiceField(disabled=True, required=False, queryset=Anime.objects.all())
    shows = forms.ModelChoiceField(disabled=True, required=False, queryset=TvShow.objects.all())


    class Meta:
        model = Comment
        fields = [
            'film',
            'anime',
            'shows',
            'comment',

        ]

