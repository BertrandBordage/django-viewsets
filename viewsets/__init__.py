# coding: utf-8

from __future__ import unicode_literals
try:
    from .base import ViewSet
    from .model_viewset import ModelViewSet
# Allows to see module metadata outside of a Django project
# (including setup.py).
except ImportError:
    pass


__author__ = 'Bertrand Bordage'
__credits__ = ('Bertrand Bordage',)
__license__ = 'BSD License'
__version__ = '0.1'
__maintainer__ = 'Bertrand Bordage'
__email__ = 'bordage.bertrand@gmail.com'
__status__ = '3 - Alpha'
