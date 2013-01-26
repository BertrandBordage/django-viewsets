# coding: utf-8

from __future__ import unicode_literals
from copy import deepcopy
from django.conf.urls import patterns, url


__all__ = (b'ViewSet',)


class ViewSet(object):
    views = {}
    excluded_views = ()
    app_label = None

    def __init__(self):
        app_label = self.app_label
        # Deep copy to allow overrides without overriding the parent class(es).
        self.views = deepcopy(self.views)
        for k in self.excluded_views:
            del self.views[k]
        self.urls = (self.__build_urls(),
                     app_label, app_label)

    def build_view_from_dict(self, view_dict):
        view = view_dict[b'view']
        for k, v in view_dict.get(b'kwargs', {}).items():
            if callable(v):
                v = v(self)
            setattr(view, k, v)
        return view

    def build_url_pattern(self, pattern):
        return pattern

    def build_url_name(self, name):
        return name

    def __build_url(self, view_dict):
        d = {
            b'regex': self.build_url_pattern(view_dict[b'pattern']),
            b'view': self.build_view_from_dict(view_dict).as_view(),
            b'name': self.build_url_name(view_dict[b'name']),
        }
        return url(**d)

    def __build_urls(self):
        return patterns(b'',
            *[self.__build_url(view_dict) for view_dict in self.views.values()]
        )
