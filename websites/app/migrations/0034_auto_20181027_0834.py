# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20181025_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stores',
            name='owners',
        ),
        migrations.AddField(
            model_name='stores',
            name='owners',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Owners'),
        ),
    ]
    
    
