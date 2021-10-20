from django.contrib import admin
from .models import Filmwork
from .models import Genre
from .models import GenreFilmwork
from .models import PersonFilmwork
from .models import Person


class GenreFilmworkInline(admin.TabularInline):
    exclude = ('id',)
    model = GenreFilmwork
    extra = 1


class PersonFilmworkInline(admin.TabularInline):
    exclude = ('id',)
    model = PersonFilmwork
    extra = 1


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):

    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type',)
    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating'
    )

    inlines = [
        GenreFilmworkInline,
        PersonFilmworkInline
    ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

    fields = (
        'name', 'description'
    )


@admin.register(Person)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'created_at', 'updated_at')

    fields = (
        'full_name', 'birth_date'
    )
