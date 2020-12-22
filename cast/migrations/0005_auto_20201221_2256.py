# Generated by Django 3.1.4 on 2020-12-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0004_tvactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('bisexual', 'Bisexual'), ('other', 'Other...')], max_length=40),
        ),
    ]
