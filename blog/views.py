# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views import View
from models import Article as Articles, UserProfile, Category
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.cache import cache


class Index(View):
    def get(self, request):
        title = '辉哥哥的主页'
        articles = Articles.objects.filter(is_delete=False).order_by('-create_date')
        return render(request, 'blog/index.html', locals())



class  Article(View):
    def get(self, request, aid):
        title = '辉哥哥的文章'
        article = Articles.objects.filter(pk=aid).first()
        if not request.user.is_superuser:
            article.views+=1
        article.save()
        return render(request, 'blog/article.html', locals())


class CategoryArticle(View):
    def get(self, request, cname):
        title = '分类页面'
        articles = Articles.objects.filter(is_delete=False).filter(category__name=cname).order_by('-create_date')
        return render(request, 'blog/category.html', locals())

class TagArticle(View):
    def get(self, request, tname):
        title = '标签页面'
        articles = Articles.objects.filter(is_delete=False).filter(tags__name=tname).order_by('-create_date')
        return render(request, 'blog/category.html', locals())

class Test(View):
    def get(self, request):
        # email_title = u'评论回复提醒'
        # content = u'您有新的回复，请注意查收。'
        # send_mail(email_title, content, settings.EMAIL_FROM, ["775470092@qq.com",], fail_silently=True)
        mag = request.user.is_superuser
        cache.clear()
        return HttpResponse(mag)
