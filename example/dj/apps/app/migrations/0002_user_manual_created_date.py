# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='manual_created_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='manual created date'),
        ),
    ]