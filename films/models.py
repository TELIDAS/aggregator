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
        return f'{self.title} {self.description} {self.image} {self.date_filmed} {self.duration} {self.age_limit} ' \
               f'{self.review}'


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

    title = models.CharField('Anime title', max_length=150)
    image = models.ImageField(upload_to='anime/')
    description = models.TextField('Anime description')
    episodes_quantity = models.PositiveSmallIntegerField('Anime episodes')
    age_limit = models.PositiveSmallIntegerField('Age limit of Anime')
    review = models.FloatField('Average review')

    def __str__(self):
        return f'{self.title}'
