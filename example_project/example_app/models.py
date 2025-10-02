# coding: utf-8

from django.db import models
from django.urls import reverse


class Example(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('example_app:example_detail', args=[self.slug])

    def __unicode__(self):
        return self.name
