# Generated by Django 3.0.7 on 2020-09-13 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200913_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='update',
            new_name='updated',
        ),
    ]