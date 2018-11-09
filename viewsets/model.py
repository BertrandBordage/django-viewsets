# coding: utf-8

from django.urls import reverse
from django.template.defaultfilters import slugify
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)

from .base import ViewSet
from .patterns import PK, PLACEHOLDER_PATTERN


__all__ = ('ModelViewSet',)


class ModelViewSet(ViewSet):
    views = {
        'list_view': {
            'view': ListView,
            'pattern': r'',
            'name': 'index',
        },
        'detail_view': {
            'view': DetailView,
            'pattern': PLACEHOLDER_PATTERN,
            'name': 'detail',
        },
        'create_view': {
            'view': CreateView,
            'pattern': r'create/',
            'name': 'create',
        },
        'update_view': {
            'view': UpdateView,
            'pattern': PLACEHOLDER_PATTERN + r'/update',
            'name': 'update',
        },
        'delete_view': {
            'view': DeleteView,
            'pattern': PLACEHOLDER_PATTERN + r'/delete',
            'name': 'delete',
        },
    }
    model = None
    base_url_pattern = None
    base_url_name = None
    id_pattern = PK
    main_view = 'list_view'
    main_url = None
    namespace = None

    def __init__(self, model=None, base_url_pattern=None, base_url_name=None,
                 id_pattern=None, excluded_views=None,
                 main_view=None, main_url=None, namespace=None):
        # Initializes parent class.
        super(ModelViewSet, self).__init__()
        # Initializes object attributes with `__init__` kwargs.
        if model is not None:
            self.model = model
        if base_url_pattern is not None:
            self.base_url_pattern = base_url_pattern
        if base_url_name is not None:
            self.base_url_name = base_url_name
        if id_pattern is not None:
            self.id_pattern = id_pattern
        if excluded_views is not None:
            self.excluded_views = excluded_views
        # The three following attributes are only used for delete_view.
        if main_view is not None:
            self.main_view = main_view
        if main_url is not None:
            self.main_url = main_url
        if namespace is not None:
            self.namespace = namespace

        # Replaces `PLACEHOLDER_PATTERN` with `id_pattern` in every view.
        for view_dict in self.views.values():
            view_dict['pattern'] = view_dict['pattern'].replace(
                PLACEHOLDER_PATTERN, self.id_pattern)

        # If not already done, initializes some attributes from model metadata.
        model_meta = self.model._meta
        if self.base_url_pattern is None:
            self.base_url_pattern = slugify(model_meta.verbose_name_plural)
        if self.base_url_name is None:
            self.base_url_name = slugify(model_meta.verbose_name)

        # Calculates `success_url` for the delete view.
        if 'delete_view' in self.views:
            if self.main_url is None:
                if self.main_view not in self.views:
                    raise Exception('%s: `main_view` not in `views`.'
                                    % self.__class__)
                main_view_name = self.views.get(self.main_view).get('name')
                self.main_url = '%s_%s' % (self.base_url_name, main_view_name)
                if self.namespace is not None:
                    self.main_url = self.namespace + ':' + self.main_url

            self.views['delete_view']['kwargs'] = {
                'get_success_url': lambda view_self: reverse(self.main_url),
            }

    def build_url_pattern(self, pattern):
        pattern = super(ModelViewSet, self).build_url_pattern(pattern)
        if self.base_url_pattern:
            return r'^%s/%s$' % (self.base_url_pattern, pattern)
        return r'^%s$' % pattern

    def build_url_name(self, name):
        name = super(ModelViewSet, self).build_url_name(name)
        return '%s_%s' % (self.base_url_name, name)

    def build_view_from_dict(self, view_dict):
        View = super(ModelViewSet, self).build_view_from_dict(view_dict)
        View.model = self.model
        return View
