# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20170501_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='invalidationDate',
            field=models.DateTimeField(),
        ),
    ]
