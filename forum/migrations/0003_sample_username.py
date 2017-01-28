# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('forum', '0002_auto_20170123_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='users.User', verbose_name='users'),
            preserve_default=False,
        ),
    ]
