# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20170208_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionboxplugin',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
