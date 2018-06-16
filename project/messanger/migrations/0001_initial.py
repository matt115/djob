# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 03:32
from __future__ import unicode_literals

from django.conf import settings
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import messanger.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_at', messanger.models.DataJSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('message', models.TextField(max_length=200)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupConversation',
            fields=[
                ('conversation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='messanger.Conversation')),
            ],
            bases=('messanger.conversation',),
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='messanger.Conversation'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='first_message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_message', to='messanger.Message'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='last_message',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_message', to='messanger.Message'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]