from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.conf import settings

__all__ = (
    'User',
)


class User(AbstractUser):
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username
