from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

# from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    LIBRARIAN = 1
    User = 2

    ROLE_CHOICES = (
        (LIBRARIAN, 'Librarian'),
        (User, 'User')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    role = models.SmallIntegerField(choices=ROLE_CHOICES,default=2)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
