# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 13:43
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0002_auto_20171029_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingpresence',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='training'),
        ),
    ]
