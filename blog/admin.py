# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_date', 'category', 'status')
    filter_horizontal = ('tags',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'email')
