from django.contrib import admin
from .models import FilmWork
from .models import Genre
from .models import GenreFilmWork
from .models import PersonFilmWork
from .models import Person


class GenreFilmWorkInline(admin.TabularInline):
    exclude = ('id',)
    model = GenreFilmWork
    extra = 1


class PersonFilmWorkInline(admin.TabularInline):
    exclude = ('id',)
    model = PersonFilmWork
    extra = 1


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):

    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type',)
    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating'
    )

    inlines = [
        GenreFilmWorkInline,
        PersonFilmWorkInline
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
