# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_auto_20170128_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionorder',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]