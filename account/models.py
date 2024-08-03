from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    dashboard_id = models.CharField(max_length=255, unique=True)
