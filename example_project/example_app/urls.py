# coding: utf-8

from __future__ import unicode_literals
from django.conf.urls import url, patterns, include
from .views import ExampleViewSet, other_example_viewset


urlpatterns = patterns(b'',
    url(br'', include(other_example_viewset.urls)),
    url(br'', include(ExampleViewSet().urls)),
)
