# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework_jwt.utils import jwt_payload_handler


class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        # if not email:
        #     raise ValueError('The given email must be set')
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

class Users(AbstractBaseUser):
    first_name = models.CharField(_('first name'), max_length=256, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=256, blank=True, null=True)
    username = models.CharField(max_length=10, unique=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    objects = CustomUserManager()

    def __str__(self):
        return str(self.pk)

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def create_jwt(self):
        """Function for creating JWT for Authentication Purpose"""
        payload = jwt_payload_handler(self)
        token = jwt.encode(payload, settings.SECRET_KEY)
        auth_token = token.decode('unicode_escape')
        return auth_token


class Post(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
