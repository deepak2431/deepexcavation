# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 20:57
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
        ('website', '0016_auto_20170208_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialsBoxPlugin',
            fields=[
                ('link_url', models.URLField(blank=True, default='', help_text='Provide a valid URL to an external website.', verbose_name='External link')),
                ('link_mailto', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email address')),
                ('link_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('link_anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('link_target', models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Target')),
                ('link_attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('title', models.CharField(max_length=255)),
                ('info', models.CharField(blank=True, max_length=255, null=True)),
                ('who', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.CharField(blank=True, max_length=255, null=True)),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='website_testimonialsboxplugin', serialize=False, to='cms.CMSPlugin')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_box_images', to='filer.Image')),
                ('link_file', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='File')),
                ('link_page', cms.models.fields.PageField(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin', models.Model),
        ),
    ]
