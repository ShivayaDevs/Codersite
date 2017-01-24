# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('forum', '0004_auto_20170123_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='username',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
        migrations.AddField(
            model_name='answers',
            name='quesID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Question'),
        ),
        migrations.AddField(
            model_name='answers',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]