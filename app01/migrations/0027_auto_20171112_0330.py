# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_buycar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buycar',
            name='cart_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Admin'),
        ),
        migrations.RemoveField(
            model_name='buycar',
            name='product',
        ),
        migrations.AddField(
            model_name='buycar',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='app01.News'),
        ),
    ]
