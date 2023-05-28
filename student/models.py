from django.db import models
from django.conf import settings

from account.models import Account
from teacher.models import Group, Question, Test


class AccountStatistics(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, related_name='stats')
    balance = models.PositiveIntegerField('Баланс', default=0)
    groups = models.ManyToManyField(Group, blank=True)
    score = models.PositiveIntegerField('Очки', default=0)
    experience = models.PositiveIntegerField('Опыт', default=0)
    lvl = models.PositiveIntegerField('Уровень', default=0)

    def __str__(self):
        return f'STATS {self.account}'

    class Meta:
        verbose_name = 'Статистика пользователя'
        verbose_name_plural = 'Статистика пользователей'


class Hero(models.Model):
    photo = models.ImageField(upload_to='main/static/photos/hero/', blank=True)
    name = models.CharField(max_length=100, default='Hero')

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class Protagonist(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    hero = models.ManyToManyField(Hero, null=True)
    name = models.CharField(max_length=100, default='Protagonist')
    health = models.PositiveIntegerField('Здоровье', default=100)
    endurance = models.PositiveIntegerField('Выносливость', default=5)
    power = models.PositiveIntegerField('Сила', default=5)
    resistance = models.IntegerField('Стойкость', default=0)
    up_score = models.PositiveIntegerField('Очки навыков', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


type_of_equipment = [
    ('wp', 'weapon'),
    ('hm', 'helmet'),
    ('sp', 'shoulder_pads'),
    ('bp', 'breastplate'),
    ('gl', 'gloves'),
    ('tr', 'trousers'),
    ('sh', 'shoes'),
]


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True )
    number_answer = models.IntegerField()
    lock_other = models.BooleanField(default=False)


class TestRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    user_name = models.CharField('ФИО', max_length=100, default='')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    count_correct = models.IntegerField("Количество верных ответов", default=0)
    grades = models.IntegerField('Оценка', default=0)
    count_points = models.IntegerField('Количество заработнанных баллов', default=0)
    created = models.DateTimeField(auto_now_add=True)

