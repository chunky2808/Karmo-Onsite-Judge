# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-08 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karmo', '0006_contest_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inpt', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('outp', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='solution',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Name',
            field=models.TextField(max_length=4000, unique=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='Timings',
            field=models.CharField(max_length=244),
        ),
        migrations.AlterField(
            model_name='contest',
            name='date',
            field=models.CharField(max_length=244),
        ),
        migrations.AddField(
            model_name='testcase',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcase_contest', to='karmo.Contest'),
        ),
        migrations.AddField(
            model_name='testcase',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testcase_ques', to='karmo.Question'),
        ),
    ]
