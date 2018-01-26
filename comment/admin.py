# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('belong', 'reply', 'create_date')