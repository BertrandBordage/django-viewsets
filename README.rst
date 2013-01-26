===============
django-viewsets
===============

.. contents::

Problematic
===========

When having a look at *Ruby on Rails*, I discovered a nice feature that was
missing in Django:
`controllers <http://guides.rubyonrails.org/action_controller_overview.html>`_.
Contrary to what I often read, views in Django are not really equivalent to
controllers in Rails.  A Rails controller basically is **a set of Django
views and Django URL patterns**.  Apart from driving off boring URL work, this
is a clean way to group views that belongs to the same model.

Any good djangonaut would make the connection with generic views − especially
`class-based <https://docs.djangoproject.com/en/1.5/topics/class-based-views/>`_.
This is the easiest solution to avoid repeating the same code with a few
changes.  But this is not simplifying URL patterns and we often have to define
such files:

::

    # views.py
    from django.views.generic import ListView, DetailView  # and so on…
    from .models import Example


    class ExampleListView(ListView):
        model = Example


    class ExampleDetailView(DetailView):
        model = Example

    # and so on…

::

    # urls.py
    from django.conf.urls import patterns, url
    from .views import *


    urlpatterns = patterns('',
        url('^examples/$', ExampleListView.as_view(), name='example_index'),
        url('^examples/(?P<pk>\d+)$', ExampleDetailView.as_view(),
            name='example_detail'),
        # and so on…
    )

With a single model, this looks easy.  With complex applications containing
dozens of models, **this looks painful** − and definitely not DRY_.

.. [DRY] Don't Repeat Yourself



Solution
========

*django-viewsets* proposes a solution inspired of Rails controllers.
``ViewSet`` is a class that builds a set of URL patterns from a set of
class-based generic views.  It is designed to be overridable, so that it fits
standard as well as advanced use.


Installation
============

``[sudo] pip install django-viewsets``

You don't have to change your project `settings.py`.


Usage
=====

``ModelViewSet``
----------------

In your application `views.py`::

    from viewsets import ModelViewSet
    from .models import YourModel

    class YourModelViewSet(ModelViewSet):
        model = YourModel


In your application `urls.py`::

    from django.conf.urls import patterns, url, include
    from .views import YourModelViewSet

    urlpatterns = patterns('',
        url('', include(YourModelViewSet().urls)),
    )

That's it!  ``ModelViewSet`` provides you these views and urls − based on the
model ``verbose_name_plural``:

============== =========================
 Generic view             URL
-------------- -------------------------
``ListView``   *your-models/*
``DetailView`` *your-models/[pk]*
``CreateView`` *your-models/create*
``UpdateView`` *your-models/[pk]/update*
``DeleteView`` *your-models/[pk]/delete*
============== =========================

To override *your-models* in all URLs, set the attribute ``base_url``.

To remove some views from the viewset, set the attribute ``excluded_views`` to
a sequence of keys of the views dict.
For example: ``('create_view', 'delete_view',)``.
