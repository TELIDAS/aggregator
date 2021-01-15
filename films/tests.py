from datetime import date

from django.test import TestCase, Client
from django.test.html import HTMLParseError

from .parser import parser
from films.forms import CommentForm, ParserForm
from films.models import Film, Anime, TvShow, Comment
from users.models import CustomUser
from .views import ParserAnimeView


class TestParser(TestCase):

    def test_parser_functions(self):
        global dom
        payload = {
            'title': 'Gekidol',
            'image': 'https://animekisa.tv/img/coversjpg/gekidol.jpg.webp?115'
        }
        try:
            dom = parser()
        except AttributeError:
            print('typeerror')
        self.assertTrue(dom)

    def test_parser_form(self):
        data = {'title': 'Gekidol',
                'image': 'https://animekisa.tv/img/coversjpg/gekidol.jpg.webp?115'
                }
        form_parser = ParserForm(data)
        is_valid = form_parser.is_valid()
        self.assertTrue(is_valid)
        form_parser.save()


    def test_parser_views(self):
        data = {'title': 'Gekidol',
                'image': 'https://animekisa.tv/img/coversjpg/gekidol.jpg.webp?115'
                }
        ParserAnimeView()
        client = Client()
        user = CustomUser.objects.create(age=101, username='text')
        client.force_login(user)
        response = client.get(path=f'/anime/')
        self.assertEqual(response.status_code, 200)


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
            'duration': 'baby',
            'age_limit': 100,
            'review': 100,
        }
        with self.assertRaises(ValueError):
            film = Film.objects.create(**payload)

    def test_update_model_film(self):
        new_title = 'New Title2'
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        film.title = new_title
        film.save()
        film.refresh_from_db()
        self.assertEqual(film.title, new_title)

    def test_delete_model_film(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'duration': 100,
            'age_limit': 100,
            'review': 100,
        }
        film = Film.objects.create(**payload)
        pk = film.pk
        film.delete()
        with self.assertRaises(Film.DoesNotExist):
            Film.objects.get(pk=pk)

    def test_create_model_anime_success(self):
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

    def test_create_model_anime_fail(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 100,
            'age_limit': 'baby',
            'review': 100,
        }
        with self.assertRaises(ValueError):
            anime = Anime.objects.create(**payload)

    def test_update_model_anime(self):
        new_title = 'New Title 2'
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        anime = Anime.objects.create(**payload)
        anime.title = new_title
        anime.save()
        anime.refresh_from_db()
        self.assertEqual(anime.title, new_title)

    def test_create_model_shows_success(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'age_limit': 100,
            'review': 100,
        }
        shows = TvShow.objects.create(**payload)
        self.assertEqual(shows.title, payload['title'])
        self.assertEqual(shows.description, payload['description'])

    def test_create_model_shows_fail(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'episodes_quantity': 100,
            'age_limit': 'hai',
            'review': 100,
        }
        with self.assertRaises(ValueError):
            shows = TvShow.objects.create(**payload)

    def test_update_model_shows(self):
        new_title = 'New Title two'
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        shows = TvShow.objects.create(**payload)
        shows.title = new_title
        shows.save()
        shows.refresh_from_db()
        self.assertEqual(shows.title, new_title)

    def test_delete_model_shows(self):
        payload = {
            'title': 'New title',
            'description': 'New Description',
            'date_filmed': date.today(),
            'episodes_quantity': 100,
            'age_limit': 100,
            'review': 100,
        }
        shows = TvShow.objects.create(**payload)
        pk = shows.pk
        shows.delete()
        with self.assertRaises(TvShow.DoesNotExist):
            TvShow.objects.get(pk=pk)


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
        data = {'film': film}
        form = CommentForm(data)
        is_valid = form.is_valid()
        self.assertFalse(is_valid)

        with self.assertRaises(ValueError):
            form.save()

        with self.assertRaises(Comment.DoesNotExist):
            comment = Comment.objects.get(pk=1)

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
        comment_text = 'Boruto sucks!!!!!'
        data = {'film': film, 'comment': comment_text}
        form = CommentForm(data)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

        form.save()
        comment = Comment.objects.all().first()
        self.assertEqual(comment.comment, data['comment'])

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

    def test_get_successful(self):
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
        user = CustomUser.objects.create(age=101, username='text')
        client.force_login(user)
        response = client.get(path=f'/films/{film.pk}/')
        self.assertEqual(response.status_code, 200)
