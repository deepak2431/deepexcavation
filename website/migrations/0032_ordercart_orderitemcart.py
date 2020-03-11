# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-16 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_auto_20170516_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='OrderItemCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='website.OrderCart')),
                ('modules', models.ManyToManyField(to='website.SoftwareModule')),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.SoftwareProductPricing')),
            ],
            options={
                'verbose_name': 'Cart item',
                'verbose_name_plural': 'Cart items',
            },
        ),
    ]
