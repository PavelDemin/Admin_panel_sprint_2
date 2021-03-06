# Generated by Django 3.2 on 2021-10-23 14:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL('CREATE SCHEMA IF NOT EXISTS content;'),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='creation date')),
                ('certificate', models.TextField(blank=True, null=True, verbose_name='certificate')),
                ('file_path', models.FileField(blank=True, null=True, upload_to='film_works/', verbose_name='file')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='rating')),
                ('type', models.CharField(choices=[('movie', 'movie'), ('tv_show', 'TV Show')], max_length=50, verbose_name='type')),
            ],
            options={
                'verbose_name': 'filmwork',
                'verbose_name_plural': 'filmworks',
                'db_table': '"content"."film_work"',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': '"content"."genre"',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
                ('birth_date', models.DateField(null=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': '"content"."person"',
            },
        ),
        migrations.CreateModel(
            name='PersonFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('role', models.CharField(max_length=255, null=True, verbose_name='role')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
            options={
                'db_table': '"content"."person_film_work"',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'db_table': '"content"."genre_film_work"',
            },
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genres',
            field=models.ManyToManyField(through='movies.GenreFilmWork', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmWork', to='movies.Person'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'person', 'role'), name='unique_person_film_work'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre'), name='unique_genre_film_work'),
        ),
    ]
