# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-20 18:36
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0063_auto_20180831_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionboxplugin',
            name='background_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='promotionboxplugin',
            name='text_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18, null=True),
        ),
    ]
