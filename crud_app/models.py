# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ErrorStack(models.Model):
    request = models.TextField()
    response = models.TextField(null=True)
    method = models.CharField(max_length=10, null=True)
    error = models.CharField(max_length=5, null=True)
    error_stack = models.TextField(null=True)
    created_date = models.DateTimeField(null=True)
    modified_date = models.DateTimeField(null=True)