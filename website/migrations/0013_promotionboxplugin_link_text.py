# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_promotionboxplugin_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionboxplugin',
            name='link_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
