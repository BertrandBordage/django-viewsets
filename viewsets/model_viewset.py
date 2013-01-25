# coding: utf-8

from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, \
                                 UpdateView, DeleteView
from django.template.defaultfilters import slugify
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse


class ModelViewSet(object):
    model = None
    views = (b'list_view', b'detail_view', b'create_view', b'update_view',
             b'delete_view')
    base_url = None
    main_view = b'list_view'
    main_url = None

    def __init__(self):
        if self.base_url is None:
            self.base_url = slugify(self.model._meta.verbose_name_plural)
        self.model_slug = slugify(self.model._meta.verbose_name)
        app_label = self.model._meta.app_label
        if self.main_url is None:
            self.main_url = b'%s:%s_%s' % (app_label,
                                           self.model_slug,
                                           getattr(self, self.main_view).name)

        self.urls = (self.__build_url_patterns(),
                     app_label, app_label)

    def __get_url(self, view_method):
        d = {
            b'regex': br'^%s$' % br'/'.join((self.base_url,
                                             view_method.pattern)),
            b'view': view_method(),
            b'name': b'%s_%s' % (self.model_slug, view_method.name),
        }
        return url(**d)

    def __build_url_patterns(self):
        return patterns(b'',
            *[self.__get_url(getattr(self, view)) for view in self.views]
        )

    def __build_model_generic_view(self, view, **kwargs):
        view.model = self.model
        for k, v in kwargs.items():
            setattr(view, k, v)
        return view.as_view()

    def list_view(self):
        return self.__build_model_generic_view(ListView)
    list_view.pattern = br''
    list_view.name = b'index'

    def detail_view(self):
        return self.__build_model_generic_view(DetailView)
    detail_view.pattern = br'(?P<pk>\d+)'  # Change to ’id’ ?
    detail_view.name = b'detail'

    def create_view(self):
        return self.__build_model_generic_view(CreateView)
    create_view.pattern = br'create'
    create_view.name = b'create'

    def update_view(self):
        return self.__build_model_generic_view(UpdateView)
    update_view.pattern = detail_view.pattern + br'/update'
    update_view.name = b'update'

    def delete_view(self):
        get_success_url = lambda _: reverse(self.main_url)
        return self.__build_model_generic_view(DeleteView,
                                               get_success_url=get_success_url)
    delete_view.pattern = detail_view.pattern + br'/delete'
    delete_view.name = b'delete'
