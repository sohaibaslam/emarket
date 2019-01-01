from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, phone, password, display_name=None):
        if not all([email, phone, password, username]):
            raise ValueError("Email, Username and Password are required!")
        if not display_name:
            display_name = username

        user = self.model(
            email=email,
            username=username,
            phone=phone,
            display_name=display_name
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, phone, password, display_name=""):
        user = self.create_user(email, username, phone, password, display_name)
        user.is_staff = True
        user.is_superuser = True

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    phone = models.IntegerField()
    display_name = models.CharField(max_length=150)
    bio = models.CharField(max_length=200, blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return f"@{self.username}"
