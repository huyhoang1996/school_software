# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20181002_1502'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='groupuserpermissions',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='groupuserpermissions',
            name='content_type',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='groupuserpermissions',
            name='groupUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.GroupUsers'),
        ),
    ]
