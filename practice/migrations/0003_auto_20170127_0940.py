# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('practice', '0002_auto_20170125_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='input_file',
        ),
        migrations.RemoveField(
            model_name='question',
            name='output_file',
        ),
        migrations.AddField(
            model_name='userquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Question'),
        ),
        migrations.AddField(
            model_name='userquestion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
