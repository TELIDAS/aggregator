# Generated by Django 3.1.4 on 2020-12-21 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_anime_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='films',
        ),
    ]
