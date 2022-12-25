from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
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

    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    patronymic = models.CharField('Отчество', max_length=255, null=True)

    location = models.CharField('Место учебы', max_length=50, blank=True, null=True, choices=locations)
    school_number = models.PositiveIntegerField('Номер школы', blank=True, null=True)
    email = models.EmailField('Электронная почта', max_length=255, blank=True, unique=True)
    # date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    # last_time_visit = models.DateTimeField(default=timezone.now)
    # is_active = models.BooleanField(default=True)

    is_teacher = models.BooleanField('Учитель', default=False, null=True)
    gender = models.CharField('Пол', max_length=50, blank=True, null=True, choices=genders)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
