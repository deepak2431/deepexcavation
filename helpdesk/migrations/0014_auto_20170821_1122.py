# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 15:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0013_auto_20170513_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='public',
            field=models.BooleanField(default=False, editable=False, help_text='Public tickets are viewable by the submitter and all staff, but non-public tickets can only be seen by staff.', verbose_name='Public'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
