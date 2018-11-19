# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id_contry', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id_state', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Countries')),
            ],
        ),
    ]