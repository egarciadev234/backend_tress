# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='states',
            name='country',
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
        migrations.DeleteModel(
            name='States',
        ),
    ]
