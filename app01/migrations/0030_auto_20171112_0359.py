# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0029_buycar_total_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BuyCar',
            new_name='BuyCart',
        ),
        migrations.AlterModelTable(
            name='buycart',
            table='BuyCart',
        ),
    ]
