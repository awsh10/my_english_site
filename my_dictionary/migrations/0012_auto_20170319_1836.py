# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 16:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_dictionary', '0011_auto_20170319_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='englishword',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 19, 16, 36, 53, 55330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 19, 16, 36, 53, 76416, tzinfo=utc)),
        ),
    ]