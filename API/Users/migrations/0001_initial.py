# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-01 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('Cellphone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('context', models.CharField(max_length=200)),
                ('time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('Cellphone', models.CharField(max_length=200)),
            ],
        ),
    ]