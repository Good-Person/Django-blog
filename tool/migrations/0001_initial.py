# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 06:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovePark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u79fb\u52a8\u65b9\u6848')),
            ],
            options={
                'verbose_name': '\u79fb\u52a8\u65b9\u6848',
                'verbose_name_plural': '\u79fb\u52a8\u65b9\u6848',
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_null', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_Parking', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u505c\u8f66\u4f4d',
                'verbose_name_plural': '\u505c\u8f66\u4f4d',
            },
        ),
        migrations.AddField(
            model_name='movepark',
            name='parking',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='move_park', to='tool.Parking'),
        ),
    ]
