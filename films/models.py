from django.db import models


# Create your models here.
class Film(models.Model):
    """
    Model for storing films with their Cast.
    """
    title = models.CharField('Film Title', max_length=150)
    image = models.ImageField(upload_to='films/', null=True)
    description = models.TextField('Film description')
    date_filmed = models.DateField('Date Filmed')
    duration = models.PositiveSmallIntegerField('Film duration')
    age_limit = models.PositiveSmallIntegerField('Age limit', default=3)
    review = models.FloatField('Average review')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    """
    comments for films
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments_film', null=True)
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='comments_anime', null=True)
    shows = models.ForeignKey('TvShow', on_delete=models.CASCADE, related_name='comments_shows', null=True)

    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class TvShow(models.Model):
    title = models.CharField('TvShow Title', max_length=150)
    image = models.ImageField(upload_to='shows/')
    description = models.TextField('Show description')
    date_filmed = models.DateField('Show Date Filmed')
    episodes_quantity = models.PositiveSmallIntegerField('Show episodes')
    age_limit = models.PositiveSmallIntegerField('Age limit', default=3)
    review = models.FloatField('Average review')

    def __str__(self):
        return f'{self.title}'



class Anime(models.Model):
    title = models.CharField('Anime title', max_length=150, null=True)
    image = models.ImageField(upload_to='anime/')
    description = models.TextField('Anime description', null=True)
    episodes_quantity = models.PositiveSmallIntegerField('Anime episodes', null=True)
    age_limit = models.PositiveSmallIntegerField('Age limit of Anime', null=True)
    review = models.FloatField('Average review', null=True)

    def __str__(self):
        return f'{self.title}'
