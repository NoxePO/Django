# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 12:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_workers'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orderName',
            field=models.CharField(default=datetime.datetime(2016, 4, 3, 12, 2, 51, 65318, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]