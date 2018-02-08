# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail

from models import *
from blog.models import Article
from django.conf import settings



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

        # 添加完评论发送邮件提醒我。
        email_title = u'博客有新评论'
        url = 'http://huigege.xin/blog/article/%d'% belong.id
        email_content = u'{}的文章下有新的评论<a href="{}">查看博客</a>'.format(belong.title, url)
        send_mail(email_title, '', settings.EMAIL_FROM, ["775470092@qq.com",], fail_silently=True, html_message=email_content)
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
