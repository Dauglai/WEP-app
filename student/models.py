from django.db import models
from django.conf import settings
from teacher.models import Group

class Account_Statistics(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    groups = models.ManyToManyField(Group)
    score = models.PositiveIntegerField('Очки', default=0)
    experience = models.PositiveIntegerField('Опыт', default=0)
    lvl = models.PositiveIntegerField('Уровень', default=0)

    class Meta:
        verbose_name = 'Статистика пользователя'
        verbose_name_plural = 'Статистика пользователей'
