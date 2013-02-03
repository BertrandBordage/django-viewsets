# coding: utf-8

from __future__ import unicode_literals


# String used to be replaced with another pattern.
PLACEHOLDER_PATTERN = br'{{ pattern_here }}'

#
# Valid patterns
#

PK = br'(?P<pk>\d+)'  # Same as id, but more generic.  See
# https://docs.djangoproject.com/en/1.4/topics/db/queries/#the-pk-lookup-shortcut
# for further information.
SLUG = br'(?P<slug>[\w-]+)'
