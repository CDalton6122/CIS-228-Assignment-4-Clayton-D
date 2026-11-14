"""
Clayton Dalton
CIS 228
Date (11-13-26)
"""

from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")