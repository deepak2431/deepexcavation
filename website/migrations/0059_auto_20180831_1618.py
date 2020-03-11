# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-31 20:18
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0058_softwaredownloadplugin_button_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwarepricingplugin',
            name='add_to_cart_button_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='softwarepricingplugin',
            name='buy_now_button_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='softwarepricingplugin',
            name='show_add_to_cart_button',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='softwarepricingplugin',
            name='show_buy_now_button',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='softwarespecificpricingplugin',
            name='add_to_cart_button_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='softwarespecificpricingplugin',
            name='buy_now_button_color',
            field=colorfield.fields.ColorField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='softwarespecificpricingplugin',
            name='show_add_to_cart_button',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='softwarespecificpricingplugin',
            name='show_buy_now_button',
            field=models.BooleanField(default=True),
        ),
    ]
