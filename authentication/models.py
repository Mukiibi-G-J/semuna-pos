from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, Group
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
