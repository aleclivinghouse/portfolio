# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class portPiece(models.Model):
    name = models.CharField(max_length=120, default="default text")
    description = models.TextField(default="default text")
    link = models.CharField(max_length=120, default="no link available")
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
