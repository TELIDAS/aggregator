from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
from django.db import models

class CustomUserManager(UserManager):
    def _create_user(self, username, age,  password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, age=age, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, age, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, age, **extra_fields)

    def create_superuser(self, username, age, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, age,  **extra_fields)


class CustomUser(AbstractUser):
    """
    Class for user model
    """
    email = None
    age = models.PositiveSmallIntegerField()
    EMAIL_FIELD = None
    REQUIRED_FIELDS = [
        'age',
    ]
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username} - {self.get_full_name()}'
