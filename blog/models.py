# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    GENDER = (
        (0, u"男"), (1, u"女")
    )
    gender = models.SmallIntegerField(u"性别", choices=GENDER, default=0)




class Tag(models.Model):
    name = models.CharField(u'标签', max_length=15)


    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(u'分类', max_length=30)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_article_num(self):
        return self.category.count()


class Article(models.Model):
    STATUS_CHOICE = (
        (0, u'个人作品'),
        (1, u'转载'),
    )

    status = models.SmallIntegerField(u'文章来源', default=0, choices=STATUS_CHOICE)
    title = models.CharField(u'文章标题', max_length=30)
    summary = models.TextField(u'文章摘要', max_length=200)
    body = models.TextField(u'文章内容')
    img_link = models.CharField(u'图片地址', max_length=255)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True)
    views = models.IntegerField(u'阅览量', default=0)
    is_delete = models.BooleanField(default=False)

    user = models.ForeignKey('UserProfile', related_name='user')
    category = models.ForeignKey('Category', related_name='category', null=True)
    tags = models.ManyToManyField('Tag', related_name='tags')

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    def get_comments(self):
        # return self.objects.filter(belong__replay=None)
        return self.belong.filter(reply=None)

    def get_comment_num(self):
        return self.belong.filter(reply=None).count()

    def get_reply_num(self):
        return self.belong.filter().exclude(reply=None).count()
