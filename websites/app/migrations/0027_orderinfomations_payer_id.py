# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20181018_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfomations',
            name='payer_id',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='payer_id'),
        ),
    ]
