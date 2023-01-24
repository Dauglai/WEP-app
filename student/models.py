from django.db import models
from django.conf import settings

from accounts.models import Account
from teacher.models import Group

class Account_Statistics(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, related_name='stats')
    groups = models.ManyToManyField(Group, blank=True)
    score = models.PositiveIntegerField('Очки', default=0)
    experience = models.PositiveIntegerField('Опыт', default=0)
    lvl = models.PositiveIntegerField('Уровень', default=0)

    def __str__(self):
        return f'STATS {self.account}'

    class Meta:
        verbose_name = 'Статистика пользователя'
        verbose_name_plural = 'Статистика пользователей'
