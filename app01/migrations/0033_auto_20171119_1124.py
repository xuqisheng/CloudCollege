# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0032_goodslist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodslist',
            options={'verbose_name': '购买清单', 'verbose_name_plural': '购买清单'},
        ),
    ]
