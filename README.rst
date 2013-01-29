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
dozens of models, **this looks painful** − and definitely not DRY [1]_.


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

============== ========================= ===================
 Generic view             URL                 URL name
-------------- ------------------------- -------------------
``ListView``   *your-models/*            *your-model_index*
``DetailView`` *your-models/[pk]*        *your-model_detail*
``CreateView`` *your-models/create*      *your-model_create*
``UpdateView`` *your-models/[pk]/update* *your-model_update*
``DeleteView`` *your-models/[pk]/delete* *your-model_delete*
============== ========================= ===================


Attributes
..........

``views``
  Dictionary defining views and URLs.  CRUD [2]_ by default.

``base_url``
  Overrides *your-models* in all URLs.  Calculated from
  ``model._meta.verbose_name_plural`` if unset.

``excluded_views``
  A sequence of keys from the ``views``.  Unset by default.
  Example: ``('create_view', 'delete_view',)``.

``namespace``
  Set this if your application has a URL namespace.  It is used to redirect
  to ``main_view`` in delete_view.  You can also set ``main_url``.

``main_view``
  Used to calculate ``main_url``.  ``'list_view'`` by default.

``main_url``
  The main url where delete_view redirects.  If set, ``main_view`` is ignored.

``model_slug``
  Used to construct URL names.  Calculated from
  ``model._meta.verbose_name`` if unset.


.. [1] Don't Repeat Yourself
.. [2] Create Read Update Delete
