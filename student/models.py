from django.db import models
from django.conf import settings

from accounts.models import Account
from teacher.models import Group, Question, Test


class Account_Statistics(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True, related_name='stats')
    groups = models.ManyToManyField(Group, blank=True)
    experience = models.PositiveIntegerField('Опыт', default=0)
    lvl = models.PositiveIntegerField('Уровень', default=0)

    def __str__(self):
        return f'STATS {self.account}'

    class Meta:
        verbose_name = 'Статистика пользователя'
        verbose_name_plural = 'Статистика пользователей'


class Protagonist(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='main/static/photos/heroes/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=100, default='Hero')
    health = models.PositiveIntegerField('Здоровье', default=100)
    power = models.PositiveIntegerField('Сила', default=5)
    resistance = models.IntegerField('Стойкость', default=0)
    up_score = models.PositiveIntegerField('Очки навыков', default=0) #За них происходит улучшение параметров

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

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
    question = models.OneToOneField(Question, on_delete=models.DO_NOTHING)
    number_answer = models.IntegerField()
    lock_other = models.BooleanField(default=False)


class Test_Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    test = models.OneToOneField(Test, on_delete=models.DO_NOTHING)
    count_correct = models.IntegerField("Количество верных ответов")
    count_points = models.IntegerField('Количество заработнанных баллов')
    created = models.DateTimeField(auto_now_add=True)

