# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_auto_20170905_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentdata',
            name='course_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='课程价格(默认免费)'),
        ),
    ]
