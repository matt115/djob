# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0003_auto_20180501_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='_message',
            new_name='message',
        ),
    ]