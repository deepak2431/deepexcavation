# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-31 20:08
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0057_auto_20180517_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwaredownloadplugin',
            name='button_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18),
        ),
    ]
