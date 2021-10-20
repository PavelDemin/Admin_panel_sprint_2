from uuid import uuid4
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(TimeStampedMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    name = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')
        db_table = '"content"."genre"'


class GenreFilmwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    film_work = models.ForeignKey('Filmwork', to_field='id', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', to_field='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"content"."genre_film_work"'
        constraints = [
            UniqueConstraint(fields=['film_work', 'genre'], name='unique_genre_film_work')
        ]


class FilmworkType(models.TextChoices):
    MOVIE = 'movie', _('movie')
    TV_SHOW = 'tv_show', _('TV Show')


class Filmwork(TimeStampedMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    creation_date = models.DateField(_('creation date'), blank=True, null=True)
    certificate = models.TextField(_('certificate'), blank=True, null=True)
    file_path = models.FileField(_('file'), upload_to='film_works/', blank=True, null=True)
    rating = models.FloatField(_('rating'), validators=[MinValueValidator(0)], blank=True, null=True)
    type = models.CharField(_('type'), max_length=50, choices=FilmworkType.choices)
    genres = models.ManyToManyField(Genre, through='GenreFilmwork')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('filmwork')
        verbose_name_plural = _('filmworks')
        db_table = '"content"."film_work"'


class Person(TimeStampedMixin, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    full_name = models.CharField(_('full name'), max_length=255)
    birth_date = models.DateField(_('date'), null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
        db_table = '"content"."person"'


class PersonFilmwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    film_work = models.ForeignKey('Filmwork', to_field='id', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', to_field='id', on_delete=models.CASCADE)
    role = models.CharField(_('role'), max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '"content"."person_film_work"'
        constraints = [
            UniqueConstraint(fields=['film_work', 'person', 'role'], name='unique_person_film_work')
        ]


