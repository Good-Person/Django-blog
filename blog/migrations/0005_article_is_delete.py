# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
