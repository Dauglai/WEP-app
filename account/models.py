from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Users must have an Email')

        user = self.model(
            email=email, **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class Account(AbstractBaseUser, PermissionsMixin):
    locations = [
        ('EKAT', 'Ekaterinburg'),
        ('MOS', 'Moscow'),
        ('SPB', 'Saint-Petersburg'),
    ]

    genders = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    roles = [
        ('T', 'Учитель'),
        ('S', 'Ученик'),
    ]

    id = models.AutoField(primary_key=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    patronymic = models.CharField('Отчество', max_length=255, null=True, blank=True)

    location = models.CharField('Место учебы', max_length=50, blank=True, null=True, choices=locations)
    school_number = models.PositiveIntegerField('Номер школы', blank=True, null=True)
    email = models.EmailField('Электронная почта', max_length=255, blank=True, unique=True)

    is_teacher = models.BooleanField('Учитель', default=False, null=True)
    gender = models.CharField('Пол', max_length=50, blank=True, null=True, choices=genders)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'