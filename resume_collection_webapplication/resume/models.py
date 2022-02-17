from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None):
        if not username:
            raise ValueError("username is required ! ")
        if not phone_number:
            raise ValueError("phone number is required ! ")

        user = self.model(
            username=username,
            phone_number=phone_number
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password=None):
        user = self.create_user(
            username=username,
            phone_number=phone_number,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name="username", unique=True, max_length=60)
    phone_number = models.CharField(max_length=15)
    date_joined = models.DateTimeField(verbose_name="joining date", auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    objects = MyUserManager()