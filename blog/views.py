# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views import View
from models import Article as Articles, UserProfile


class Index(View):
    def get(self, request):
        title = '辉哥哥的主页'
        articles = Articles.objects.all().order_by('-create_date')
        return render(request, 'blog/index.html', locals())



class  Article(View):
    def get(self, request, aid):
        title = '辉哥哥的文章'
        article = Articles.objects.filter(pk=aid).first()
        article.views+=1
        article.save()
        return render(request, 'blog/article.html', locals())


class Search(View):
    def get(self, request):
        title = '搜索页面'
        return render(request, 'blog/search.html', locals())


