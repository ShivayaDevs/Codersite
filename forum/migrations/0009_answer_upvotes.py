# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_question_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]