# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='bdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Neu', 'Neu'), ('Athlet', 'Athlet'), ('Eltern', 'Eltern'), ('Coach', 'Coach')], default='Neu', max_length=20),
        ),
    ]
