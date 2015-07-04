# coding: utf-8

from django.conf.urls import url, patterns, include
from .views import ExampleViewSet, other_example_viewset


urlpatterns = patterns('',
    url(r'', include(other_example_viewset.urls)),
    url(r'', include(ExampleViewSet().urls)),
)
