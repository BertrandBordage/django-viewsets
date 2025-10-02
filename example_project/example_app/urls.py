# coding: utf-8

from django.urls import path, include
from .views import OtherViewSet, example_viewset


urlpatterns = [
    path('', include((example_viewset.urls, 'example_app'), namespace='example_app')),
    path('', include((OtherViewSet().urls, 'other_app'), namespace='other_app')),
]
