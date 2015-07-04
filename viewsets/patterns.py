# coding: utf-8

# String used to be replaced with another pattern.
PLACEHOLDER_PATTERN = r'{{ pattern_here }}'

#
# Valid patterns
#

PK = r'(?P<pk>\d+)'  # Same as id, but more generic.  See
# https://docs.djangoproject.com/en/1.4/topics/db/queries/#the-pk-lookup-shortcut
# for further information.
SLUG = r'(?P<slug>[\w-]+)'
