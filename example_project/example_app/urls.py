# coding: utf-8

from __future__ import unicode_literals
from django.conf.urls import url, patterns, include
from .views import ExampleViewSet


urlpatterns = patterns(b'',
    url(br'', include(ExampleViewSet().urls)),
)
