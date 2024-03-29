# Generated by Django 3.1.14 on 2023-05-28 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='main/static/photos/enemy/%Y/%m/%d')),
                ('name', models.CharField(default='Boss', max_length=100)),
                ('health', models.PositiveIntegerField(default=100, verbose_name='Здоровье')),
                ('power', models.PositiveIntegerField(default=5, verbose_name='Сила')),
                ('resistance', models.IntegerField(default=3, verbose_name='Стойкость')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=600, null=True, verbose_name='ФИО автора')),
                ('group_name', models.CharField(max_length=300, verbose_name='Название группы')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Группа (класс)',
                'verbose_name_plural': 'Группы (классы)',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=600, null=True, verbose_name='ФИО автора')),
                ('title', models.CharField(max_length=300, verbose_name='Название теста')),
                ('subject', models.CharField(max_length=100, null=True, verbose_name='Название предмета')),
                ('text', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Дополнительный текст к тесту')),
                ('difficulty', models.PositiveIntegerField(null=True, verbose_name='Сложность')),
                ('time', models.TimeField(null=True, verbose_name='Время выполнения')),
                ('time_deadline', models.TimeField(null=True, verbose_name='Время сдачи')),
                ('date_deadline', models.DateField(null=True, verbose_name='Дата сдачи')),
                ('number_attempts', models.PositiveIntegerField(default=1, verbose_name='Количество попыток на прохождение')),
                ('five', models.PositiveIntegerField(verbose_name='Количество баллов для оценки 5')),
                ('four', models.PositiveIntegerField(verbose_name='Количество баллов для оценки 4')),
                ('three', models.PositiveIntegerField(verbose_name='Количество баллов для оценки 3')),
                ('two', models.PositiveIntegerField(verbose_name='Количество баллов для оценки 2')),
                ('boss', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.boss')),
                ('group', models.ManyToManyField(blank=True, to='teacher.Group')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Поле для ввода вопроса')),
                ('first_answer', models.CharField(max_length=250, verbose_name='Вариант ответа №1')),
                ('second_answer', models.CharField(max_length=250, verbose_name='Вариант ответа №2')),
                ('third_answer', models.CharField(max_length=250, verbose_name='Вариант ответа №3')),
                ('four_answer', models.CharField(max_length=250, verbose_name='Вариант ответа №4')),
                ('reward', models.PositiveIntegerField(null=True, verbose_name='Количество баллов')),
                ('number_correct_answer', models.PositiveIntegerField(verbose_name='Номер правильного ответа')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.test')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
