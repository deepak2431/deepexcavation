# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_promotionboxplugin_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotionboxplugin',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Only applicable with is apply hover effect'),
        ),
    ]
