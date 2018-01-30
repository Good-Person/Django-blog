# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string

from models import *
from blog.models import Article



class GetReply(View):
    def get(self, request):

        data = {
            'reply':[]
        }
        aid = request.GET.get('aid')
        article = Article.objects.filter(pk=aid).first()
        replies = article.belong.filter().exclude(reply=None).all().order_by('create_date')

        for reply in replies:
            context = {'reply':reply}
            message = render_to_string('comment/reply.html', context)
            data['reply'].append({'pid':reply.reply.id,'html':message})
        return JsonResponse(data)

class AddComment(View):
    def post(self, request):
        data = {
            'msg' : 'ok'
        }
        aid = request.POST.get('aid')
        content = request.POST.get('content')
        user = None
        belong = Article.objects.filter(pk=aid).first()
        if request.user.is_authenticated():
            user = request.user
        comment = Comment()
        comment.add_comment(content, belong, user=user)
        return JsonResponse(data)

class AddReply(View):
    def post(self, request):
        aid = request.POST.get('aid')
        pid = request.POST.get('parent')
        content = request.POST.get('content')
        user = None
        belong = Article.objects.filter(pk=aid).first()
        parent = Comment.objects.filter(pk=pid).first()
        if request.user.is_authenticated():
            user = request.user
        comment = Comment()
        comment.add_comment(content, belong, parent=parent, user=user)
        return JsonResponse({'data':'ok'})
