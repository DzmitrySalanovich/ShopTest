from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from .validators import UsernameValidator

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, full_name, password, **extra_fields):
        """
        Create and save a user with the given username, email,
        full_name, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not full_name:
            raise ValueError('The given full name must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email, username=username, full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, username, full_name, password, **extra_fields
        )

    def create_superuser(self, email, username, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            email, username, full_name, password, **extra_fields
        )


class User(PermissionsMixin, AbstractBaseUser):
    username_validators = UsernameValidator()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True, db_index=True, validators=[username_validators])
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.full_name