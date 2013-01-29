# coding: utf-8

from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, \
                                 UpdateView, DeleteView
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from .base import ViewSet


__all__ = (b'ModelViewSet',)


class ModelViewSet(ViewSet):
    model = None
    views = {
        b'list_view': {
            b'view': ListView,
            b'pattern': br'',
            b'name': b'index',
        },
        b'detail_view': {
            b'view': DetailView,
            b'pattern': br'(?P<pk>\d+)',  # Change to ’id’?
            b'name': b'detail',
        },
        b'create_view': {
            b'view': CreateView,
            b'pattern': br'create',
            b'name': b'create',
        },
        b'update_view': {
            b'view': UpdateView,
            b'pattern': br'(?P<pk>\d+)/update',  # Change to ’id’?
            b'name': b'update',
        },
        b'delete_view': {
            b'view': DeleteView,
            b'pattern': br'(?P<pk>\d+)/delete',  # Change to ’id’?
            b'name': b'delete',
        },
    }
    namespace = None
    base_url = None
    model_slug = None
    main_view = b'list_view'
    main_url = None

    def __init__(self):
        super(ModelViewSet, self).__init__()

        if self.base_url is None:
            self.base_url = slugify(self.model._meta.verbose_name_plural)
        if self.model_slug is None:
            self.model_slug = slugify(self.model._meta.verbose_name)

        if self.main_url is None:
            if self.main_view not in self.views:
                raise Exception('%s: `main_view` not in `views`.'
                                % self.__class__)
            main_view_name = self.views.get(self.main_view).get(b'name')
            self.main_url = b'%s_%s' % (self.model_slug, main_view_name)
            if self.namespace is not None:
                self.main_url = self.namespace + b':' + self.main_url

        if b'delete_view' in self.views:
            self.views[b'delete_view'][b'kwargs'] = {
                b'get_success_url': lambda view_self: reverse(self.main_url),
            }

    def build_url_pattern(self, pattern):
        pattern = super(ModelViewSet, self).build_url_pattern(pattern)
        if self.base_url:
            return br'^%s/%s$' % (self.base_url, pattern)
        return br'^%s$' % pattern

    def build_url_name(self, name):
        name = super(ModelViewSet, self).build_url_name(name)
        return b'%s_%s' % (self.model_slug, name)

    def build_view_from_dict(self, view_dict):
        View = super(ModelViewSet, self).build_view_from_dict(view_dict)
        View.model = self.model
        return View
