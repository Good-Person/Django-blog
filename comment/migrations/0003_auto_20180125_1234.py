# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 04:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20180125_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_time',
            new_name='create_date',
        ),
    ]