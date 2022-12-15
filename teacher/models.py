from django.db import models


class Test(models.Model):
    title = models.CharField('Название теста', max_length=100)
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


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    question = models.CharField('Поле для ввода вопроса', max_length=500)
    first_answer = models.CharField('Вариант ответа №1', max_length=250)
    second_answer = models.CharField('Вариант ответа №2', max_length=250)
    third_answer = models.CharField('Вариант ответа №3', max_length=250)
    four_answer = models.CharField('Вариант ответа №4', max_length=250)
    number_correct_answer = models.PositiveIntegerField('Номер правильного ответа')