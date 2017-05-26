# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-17 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Missions', '0006_attacheddoc_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='attacheddoc',
            name='activeDate',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='attacheddoc',
            name='audit',
            field=models.BooleanField(default=False),
        ),
    ]