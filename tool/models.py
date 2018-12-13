# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.models import UserProfile

class Parking(models.Model):

    is_null = models.BooleanField(default=True)
    user = models.ForeignKey(UserProfile, related_name='parking_user', blank=True, null=True)

    class Meta:
        verbose_name = u'停车位'
        verbose_name_plural = verbose_name



class MovePark(models.Model):

    content = models.TextField(u'移动方案')
    parking = models.ForeignKey(Parking, related_name='parking', blank=True)

    class Meta:
        verbose_name = u'移动方案'
        verbose_name_plural = verbose_name