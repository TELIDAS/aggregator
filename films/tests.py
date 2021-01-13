from datetime import date

from django.test import TestCase, Client

from films.forms import CommentForm
from films.models import Film, Anime, TvShow
from users.models import CustomUser


def sum_a_b(a, b):
    return a + b


def sub(a, b):
    return a - b


def calculate(a, b):
    return sum_a_b(a, b) - sub(a, b)


class TestFunction(TestCase):
    """
    Testing utility functions.
    """

    def test_sum_functions(self):
        result = sum_a_b(5, 5)
        self.assertEqual(result, 10)

    def test_sub_functions(self):
        result = sub(5, 5)
        self.assertEqual(result, 0)

    def test_calculate_function(self):
        result = calculate(5, 5)
        self.assertEqual(result, 10)


class TestModel(TestCase):
    """
    Testing film models
    """

    def test_create_model_film_success(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        self.assertEqual(film.title, payload['title'])
        self.assertEqual(film.description, payload['description'])
        self.assertEqual(film.duration, payload['duration'])

    def test_create_model_film_fail(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        payload2 = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        film2 = Film.objects.create(**payload2)
        self.assertFalse(film == film2)



    def test_update_model_film(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        Film.objects.update(**payload)

    def test_delete_model_film(self):
        film = Film.objects.all().delete()

    def test_create_model_anime(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        anime = Anime.objects.create(**payload)
        self.assertEqual(anime.title, payload['title'])
        self.assertEqual(anime.description, payload['description'])

    def test_update_model_anime(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        Anime.objects.update(**payload)



    def test_create_model_shows(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        shows = TvShow.objects.create(**payload)
        self.assertEqual(shows.title, payload['title'])
        self.assertEqual(shows.description, payload['description'])

    def test_update_model_shows(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        TvShow.objects.update(**payload)

    def test_delete_model_shows(self):
        shows = TvShow.objects.all().delete()




class TestForms(TestCase):
    """
    Testing film forms
    """

    def test_comment_creation_fail(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        comment_text = 'Boruto sucks!!!!!'
        form = CommentForm(initial={'film': film, 'comment': comment_text})
        is_valid = form.is_valid()
        self.assertFalse(is_valid)

        with self.assertRaises(Exception):
            form.save()


    def test_anime_comment_fail(self):
        payload_anime = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 12,
            'age_limit': 100,
            'review': 100,
        }
        anime = Anime.objects.create(**payload_anime)
        comment_text = 'Boruto sucks!!!!!'
        form = CommentForm(initial={'anime': anime, 'comment': comment_text})
        is_valid = form.is_valid()
        self.assertFalse(is_valid)

        with self.assertRaises(Exception):
            form.save()

    def test_shows_comment_fail(self):
        payload_shows = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 12,
            'date_filmed': '2020-10-10',
            'age_limit': 100,
            'review': 100,
        }
        shows = TvShow.objects.create(**payload_shows)
        comment_text = 'Boruto sucks!'
        form = CommentForm(initial={'shows': shows, 'comment': comment_text})
        is_valid = form.is_valid()
        self.assertFalse(is_valid)

        with self.assertRaises(Exception):
            form.save()


        """
        testing forms success
        """

    def test_comment_creation_success(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        comment_text = 'Boruto sucks!'
        form = CommentForm({'film': film, 'comment': comment_text})
        is_valid = form.is_valid()
        self.assertTrue(is_valid)
        form.save()


class TestViews(TestCase):
    """
    Testing films views
    """

    def test_not_authenticated_cant_pass(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        client = Client()
        response = client.get(path=f'/films/{film.pk}')
        self.assertEqual(response.status_code, 301)

    def test_age_limit(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        client = Client()
        user = CustomUser.objects.create(age=99, username='test')
        client.force_login(user)
        response = client.get(path=f'/films/{film.pk}/')
        self.assertEqual(response.status_code, 200)
