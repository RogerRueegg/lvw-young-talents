# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-19 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0007_competition_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='selfsubscription',
            field=models.BooleanField(default=False),
        ),
    ]
