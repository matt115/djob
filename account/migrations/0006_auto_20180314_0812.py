# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180314_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='actual_job',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]