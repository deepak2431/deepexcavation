# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-08 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0050_auto_20170908_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
