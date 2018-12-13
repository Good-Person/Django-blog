# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 07:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movepark',
            name='parking',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking', to='tool.Parking'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
