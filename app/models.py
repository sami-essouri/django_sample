from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class User(AbstractUser):
    location = models.CharField(max_length=50, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
