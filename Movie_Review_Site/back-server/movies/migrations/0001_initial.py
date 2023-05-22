# Generated by Django 3.2.13 on 2023-05-22 01:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField(unique=True)),
                ('genre_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(null=True)),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('video_path', models.CharField(blank=True, max_length=200, null=True)),
                ('popularity', models.FloatField()),
                ('actors', models.JSONField(null=True)),
                ('director', models.CharField(max_length=100, null=True)),
                ('score_average', models.FloatField()),
                ('release_date', models.DateField()),
                ('genres', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
