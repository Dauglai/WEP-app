# Generated by Django 4.1.3 on 2022-12-08 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
    ]
