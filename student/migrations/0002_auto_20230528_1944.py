# Generated by Django 3.1.14 on 2023-05-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrecord',
            name='count_correct',
            field=models.IntegerField(default=0, verbose_name='Количество верных ответов'),
        ),
        migrations.AlterField(
            model_name='testrecord',
            name='count_points',
            field=models.IntegerField(default=0, verbose_name='Количество заработнанных баллов'),
        ),
    ]
