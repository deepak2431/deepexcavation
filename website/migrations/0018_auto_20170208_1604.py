# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_testimonialsboxplugin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_anchor',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_attributes',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_file',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_mailto',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_phone',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_target',
        ),
        migrations.RemoveField(
            model_name='testimonialsboxplugin',
            name='link_url',
        ),
    ]
