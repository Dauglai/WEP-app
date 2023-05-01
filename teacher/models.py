from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse #?????

from accounts.models import Account

from django.conf import settings
from django.db import models


class Test(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    owner_name = models.CharField('ФИО автора', max_length=600, null=True)
    title = models.CharField('Название теста', max_length=300)
    subject = models.CharField('Название предмета', max_length=100, null=True)
    text = models.TextField('Дополнительный текст к тесту', max_length=1000, null=True, blank=True)
    difficulty = models.PositiveIntegerField('Сложность', null=True)
    time = models.TimeField('Время выполнения', null=True)
    time_deadline = models.TimeField('Время сдачи', null=True)
    date_deadline = models.DateField('Дата сдачи', null=True)
    five = models.PositiveIntegerField('Количество баллов для оценки 5')
    four = models.PositiveIntegerField('Количество баллов для оценки 4')
    three = models.PositiveIntegerField('Количество баллов для оценки 3')
    two = models.PositiveIntegerField('Количество баллов для оценки 2')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task', args=[self.id])

   # def get_absolute_url(self):
   #     return reverse('task', kwargs={'task_id': self.pk})

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Group(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    tasks = models.ManyToManyField(Test, blank=True)
    owner_name = models.CharField('ФИО автора', max_length=600, null=True)
    group_name = models.CharField('Название группы', max_length=300)
    login = models.CharField('Логин', max_length=50, unique=True)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа (класс)'
        verbose_name_plural = 'Группы (классы)'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    question = models.CharField('Поле для ввода вопроса', max_length=500)
    first_answer = models.CharField('Вариант ответа №1', max_length=250)
    second_answer = models.CharField('Вариант ответа №2', max_length=250)
    third_answer = models.CharField('Вариант ответа №3', max_length=250)
    four_answer = models.CharField('Вариант ответа №4', max_length=250)
    reward = models.PositiveIntegerField('Количество баллов', null=True)
    number_correct_answer = models.PositiveIntegerField('Номер правильного ответа')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
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
