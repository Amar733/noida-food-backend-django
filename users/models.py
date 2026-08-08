from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.email
