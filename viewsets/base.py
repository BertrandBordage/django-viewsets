# coding: utf-8

from __future__ import unicode_literals
from copy import deepcopy
from django.conf.urls import url


__all__ = (b'ViewSet',)


class ViewSet(object):
    views = {}
    excluded_views = ()

    def __init__(self):
        # Deep copy to allow overrides without overriding the parent class(es).
        self.views = deepcopy(self.views)
        for k in self.excluded_views:
            del self.views[k]

    def build_view_from_dict(self, view_dict):
        View = view_dict[b'view']

        class NewView(View):
            pass

        for k, v in view_dict.get(b'kwargs', {}).items():
            setattr(NewView, k, v)

        return NewView

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

    @property
    def urls(self):
        return [self.__build_url(view_dict)
                for view_dict in self.views.values()]
