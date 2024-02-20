from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    # def create_user(self, email, username, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError('The Email field must be set')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, username=username, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # mobile_number=models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
        
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def _str_(self):
        return self.email

class Role(models.Model):
    role = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')

    def _str_(self):
        return self.role

class Permissions(models.Model):
    permission = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='permissions')

    def _str_(self):
        return self.permission