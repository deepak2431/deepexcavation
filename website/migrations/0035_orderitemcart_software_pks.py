# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-16 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_orderitemcart_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemcart',
            name='software_pks',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]
