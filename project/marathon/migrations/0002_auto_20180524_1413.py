# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialrequest',
            name='tile',
            field=models.CharField(blank=True, default='', max_length=70),
        ),
    ]
