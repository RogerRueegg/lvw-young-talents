# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-17 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20171029_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bdate',
            field=models.DateField(blank=True, default='2099-01-20', null=True, verbose_name='Geburtsdatum'),
        ),
    ]
