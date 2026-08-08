from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, unique=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True, null=True)  # Make email optional

    def __str__(self):
        return self.phone if self.phone else self.username
