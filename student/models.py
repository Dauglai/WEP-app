from django.db import models
from django.conf import settings

from account.models import Account
from teacher.models import Group, Question, Test


class Account_Statistics(models.Model):
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


class Protagonist(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, default='Hero')
    health = models.PositiveIntegerField('Здоровье', default=100)
    endurance = models.PositiveIntegerField('Выносливость', default=5) #Зависит от выбранного класса
    power = models.PositiveIntegerField('Сила', default=5)
    dexterity = models.PositiveIntegerField('Ловкость', default=7)
    resistance = models.IntegerField('Стойкость', default=0)
    up_score = models.PositiveIntegerField('Очки навыков', default=0) #За них происходит улучшение параметров

    # weapon = 

    # Снаряжение, экипировка
    # helmet =
    # shoulder_pads =
    # breastplate =
    # gloves =
    # trousers =
    # shoes =

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


class Item(models.Model):
    name = models.CharField('Название', max_length=50)
    type_equipment = models.CharField(choices=type_of_equipment, max_length=2)
    description = models.CharField('Описание', max_length=200, blank=True)
    cost = models.PositiveIntegerField('Стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Inventory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, blank=True) #on_delete=models.DO_NOTHING #models.DO_NOTHING
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'INV {self.account}'

    class Meta:
        verbose_name = 'Инвентарь'
        verbose_name_plural = 'Инвентарь'


class Choice(models.Model):
    question = models.OneToOneField(Question, on_delete=models.DO_NOTHING)
    number_answer = models.IntegerField()
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title


class Test_Record(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    test = models.OneToOneField(Test, on_delete=models.DO_NOTHING)
    count_correct = models.IntegerField("Количество верных ответов")
    count_points = models.IntegerField('Количество заработнанных баллов')

