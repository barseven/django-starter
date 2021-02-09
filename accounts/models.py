from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add custom fields here

    def __str__(self):
        return self.email
