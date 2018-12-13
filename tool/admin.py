# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_null')

@admin.register(MovePark)
class MoveParkAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'parking')