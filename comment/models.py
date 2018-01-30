# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog.models import Article, UserProfile

class Comment(models.Model):

    content = models.TextField(u'评论内容')
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    user = models.ForeignKey(UserProfile, related_name='user_comment', blank=True, null=True)
    belong = models.ForeignKey(Article, related_name='belong')
    reply = models.ForeignKey('self', related_name='parent_reply', blank=True, null=True)


    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content[0:10]

    def add_comment(self, content, belong, parent=None, user=None):
        self.content = content
        self.belong = belong
        self.reply = parent
        self.user = user
        self.save()
        return self

