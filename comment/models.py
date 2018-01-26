# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.models import Article

class Comment(models.Model):

    content = models.TextField(u'评论内容')
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    belong = models.ForeignKey(Article, related_name='belong')
    reply = models.ForeignKey('self', related_name='parent_reply', null=True, default=None)


    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content[0:10]