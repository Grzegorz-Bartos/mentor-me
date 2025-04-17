from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    role = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
