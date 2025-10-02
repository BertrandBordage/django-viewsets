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
