# coding: utf-8

from django.urls import path, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # path('', 'example_project.views.home', name='home'),
    # path('example_project/', include('example_project.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # path('admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # path('admin/', include(admin.site.urls)),
    path('', include('example_app.urls')),
]
