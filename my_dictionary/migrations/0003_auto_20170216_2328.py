# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_dictionary', '0002_auto_20170216_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='english_word',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='english_word',
            name='english',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]