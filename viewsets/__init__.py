# coding: utf-8

from __future__ import unicode_literals

try:
    from django.core.exceptions import ImproperlyConfigured
except ImportError:
    ImproperlyConfigured = ImportError

try:
    from .base import ViewSet
    from .model import ModelViewSet
# Allows to see module metadata outside of a Django project
# (including setup.py).
except (ImportError, ImproperlyConfigured):
    pass

from .patterns import PK, SLUG


__author__ = 'Bertrand Bordage'
__credits__ = ('Bertrand Bordage',)
__license__ = 'BSD License'
__version__ = '0.2.0'
__maintainer__ = 'Bertrand Bordage'
__email__ = 'bordage.bertrand@gmail.com'
__status__ = '3 - Alpha'
