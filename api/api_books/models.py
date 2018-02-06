# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date


@python_2_unicode_compatible
class Author(models.Model):
    """
    These are the Author model fields.
    """
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

@python_2_unicode_compatible
class Book(models.Model):
    """
    These are the Book model fields.
    """
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=13)

    published = models.DateField(default=date.today)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u"%s" % (self.title)
