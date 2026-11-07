from django.db import models
from django.contrib.auth.models import AbstractUser
"""
Clayton Dalton
CIS 228
Date (11-07-26)
"""

class CustomUser(AbstractUser):
    pass
    # additional fields here

    def __str__(self):
        return self.username