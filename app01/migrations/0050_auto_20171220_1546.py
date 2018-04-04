# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0049_news_videos_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videos_url',
            field=models.CharField(max_length=300, verbose_name='课程列表', null=True, blank=True),
        ),
    ]
