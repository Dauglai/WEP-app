# Generated by Django 4.1.3 on 2022-12-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_test_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='deadline',
        ),
        migrations.AddField(
            model_name='test',
            name='date_deadline',
            field=models.DateField(null=True, verbose_name='Дата сдачи'),
        ),
        migrations.AddField(
            model_name='test',
            name='time_deadline',
            field=models.TimeField(null=True, verbose_name='Время сдачи'),
        ),
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True, verbose_name='Время выполнения'),
        ),
    ]
