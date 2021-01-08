from django import forms

from films.models import Comment, Film, Anime, TvShow
from films.parser import parser as anime_parser, parser_films
from films.parser import parser_shows


class CommentForm(forms.ModelForm):
    film = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                  disabled=True, required=False, queryset=Film.objects.all())
    anime = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                   disabled=True, required=False, queryset=Anime.objects.all())
    shows = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                   disabled=True, required=False, queryset=TvShow.objects.all())

    class Meta:
        model = Comment
        fields = [
            'film',
            'anime',
            'shows',
            'comment',
        ]


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Anime', 'Anime'),
        ('Film', 'Film'),
        ('TvShow', 'TvShow'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'Anime':
            anime_data = anime_parser()
            for i in anime_data:
                Anime.objects.create(**i)
        elif self.data['media_type'] == 'TvShow':
            shows_data = parser_shows()
            for b in shows_data:
                TvShow.objects.create(**b)
        elif self.data['media_type'] == 'Film':
            shows_data = parser_films()
            for l in shows_data:
                Film.objects.create(**l)
