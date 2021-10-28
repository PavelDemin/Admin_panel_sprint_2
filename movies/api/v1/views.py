from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView

from movies.models import FilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def _aggregate_person(self, role):
        return ArrayAgg('person__full_name', distinct=True, filter=Q(personfilmwork__role=role))

    def get_queryset(self):
        queryset = FilmWork.objects.prefetch_related('genres', 'persons').values(
            'id', 'title', 'description', 'creation_date', 'rating', 'type').annotate(
            genres=ArrayAgg('genres__name', distinct=True),
            actors=self._aggregate_person('actor'),
            directors=self._aggregate_person('director'),
            writers=self._aggregate_person('writer')
        )
        return queryset

    def render_to_response(self, context):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, **kwargs):
        page_num = self.request.GET.get('page', 1)
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        if page_num == 'last':
            result = paginator.page(paginator.num_pages)
        else:
            result = paginator.page(page_num)
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(result),
        }
        return context


class MovieDetailApi(MoviesApiMixin, BaseDetailView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = self.get_object(self.queryset)
        return context
