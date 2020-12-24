from django.db import models

# Create your models here.
class Cast(models.Model):
    """
    Model for storing cast of the films and shows.
    """
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('bisexual', 'Bisexual'),
        ('other', 'Other...'),
    )
    name = models.CharField("Actor's name", max_length=150)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=gender_choices, max_length=40)
    films = models.ManyToManyField('films.Film', related_name="casts")
    image = models.ImageField(upload_to='cast/', null=True)

    def __str__(self):
        return f'{self.name}'


class TvActor(models.Model):
    """
    Model for storing cast of the films and shows.
    """
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('bisexual', 'Bisexual'),
        ('other', 'Other...'),
    )
    name = models.CharField("Actor's name", max_length=150)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=gender_choices, max_length=40)
    films = models.ManyToManyField('films.TvShow', related_name="tvactors")
    image = models.ImageField(upload_to='tvactor/', null=True)

    def __str__(self):
        return f'{self.name}'


class Character(models.Model):
    """
    Model for storing characters of the anime
    """
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other...'),
    )

    name = models.CharField('Character name', max_length=150)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=gender_choices, max_length=40)
    anime = models.ManyToManyField('films.Anime', related_name="characters")
    image = models.ImageField(upload_to='Character/')

    def __str__(self):
        return f'{self.name}'
