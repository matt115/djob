# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20180607_1331'),
        ('messanger', '0005_auto_20180501_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='users',
        ),
        migrations.AddField(
            model_name='conversation',
            name='profiles',
            field=models.ManyToManyField(to='account.Profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_sended', to='account.Profile'),
        ),
    ]