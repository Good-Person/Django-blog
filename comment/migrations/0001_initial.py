# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belong', to='blog.Article')),
                ('creply', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
            },
        ),
    ]
