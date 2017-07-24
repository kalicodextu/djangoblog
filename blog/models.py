# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# BlogPost
class BlogPost(models.Model):
    title = models.CharField(max_length=160)
    author = models.CharField(max_length=160)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)