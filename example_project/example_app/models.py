# coding: utf-8

from django.db.models import permalink
from django.db import models


class Example(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()

    @permalink
    def get_absolute_url(self):
        return 'example_app:example_detail', (self.slug,)

    def __unicode__(self):
        return self.name
