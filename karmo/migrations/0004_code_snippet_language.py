# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karmo', '0003_auto_20180530_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='code_snippet',
            name='language',
            field=models.TextField(default=''),
        ),
    ]