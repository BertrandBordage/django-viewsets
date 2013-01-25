# coding: utf-8

from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, \
                                 UpdateView, DeleteView
from django.template.defaultfilters import slugify
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse
from copy import deepcopy


class ModelViewSet(object):
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
            b'pattern': br'create',  # Change to ’id’?
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
            b'kwargs': {
                b'get_success_url': lambda self:
                                        lambda _: reverse(self.main_url),
            },
        },
    }
    base_url = None
    main_view = b'list_view'
    main_url = None

    def __init__(self):
        if self.base_url is None:
            self.base_url = slugify(self.model._meta.verbose_name_plural)
        self.model_slug = slugify(self.model._meta.verbose_name)
        app_label = self.model._meta.app_label
        # Deep copy to allow overrides without overriding the parent classe(s).
        self.views = deepcopy(self.views)
        if self.main_url is None:
            main_view_name = self.views.get(self.main_view).get(b'name')
            self.main_url = b'%s:%s_%s' % (app_label,
                                           self.model_slug,
                                           main_view_name)

        self.urls = (self.__build_url_patterns(),
                     app_label, app_label)

    def __build_model_generic_view(self, view_dict):
        view = view_dict[b'view']
        view.model = self.model
        for k, v in view_dict.get(b'kwargs', {}).items():
            if callable(v):
                v = v(self)
            setattr(view, k, v)
        return view.as_view()

    def __get_url(self, view_dict):
        d = {
            b'regex': br'^%s$' % br'/'.join((self.base_url,
                                             view_dict[b'pattern'])),
            b'view': self.__build_model_generic_view(view_dict),
            b'name': b'%s_%s' % (self.model_slug, view_dict[b'name']),
        }
        return url(**d)

    def __build_url_patterns(self):
        return patterns(b'',
            *[self.__get_url(view_dict) for view_dict in self.views.values()]
        )
