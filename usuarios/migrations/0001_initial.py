# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 20:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number_identification', models.CharField(max_length=20)),
                ('cellphone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('address_location', models.CharField(max_length=255)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contributory_regimen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilities.ContributeRegimen')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilities.Countries')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilities.Rules')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilities.States')),
                ('type_identification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilities.TypeIdentification')),
            ],
        ),
    ]
