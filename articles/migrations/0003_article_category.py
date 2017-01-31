# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_auto_20170129_0622'),
        ('articles', '0002_auto_20170128_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_requests_created', to='practice.Category'),
            preserve_default=False,
        ),
    ]