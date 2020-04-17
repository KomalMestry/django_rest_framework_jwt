# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
