# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-16 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_remove_orderitemcart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemcart',
            name='name',
        ),
    ]
