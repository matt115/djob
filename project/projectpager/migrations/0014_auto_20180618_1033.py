# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20180617_1656'),
        ('projectpager', '0013_auto_20180615_1635'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projectpage',
            unique_together=set([('owner', '_name')]),
        ),
    ]