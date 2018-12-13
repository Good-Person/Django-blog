# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from django.views import View
from models import Article as Articles, UserProfile, Category
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache


import uuid
import time
from utils.dingding import get_dingding_json_data, judge_pc_or_mobile
from utils.sqlalcemyTest import Caiwu as caiwu
from utils.sqlalcemyTest import User as dinguser
from utils.sqlalcemyTest import Session


class Index(View):
    def get(self, request):
        title = '辉哥哥的主页'
        page_limit = request.GET.get('page_limit')
        page_start = request.GET.get('page_start')
        articles = Articles.objects.filter(is_delete=False).order_by('-create_date')
        if page_limit and page_start:
            result = {
                'msg':[]
            }
            if not page_start.isdigit() and not page_limit.isdigit():
                return JsonResponse(result)

            page_start = int(page_start)
            page_limit = int(page_limit)+page_start
            for article in articles[page_start:page_limit]:
                item = {}
                item['atitle'] = article.title
                item['aurl'] = '/blog/article/?aid={}'.format(article.id)
                item['user'] = article.user.username
                item['create_date'] = article.create_date.strftime("%Y-%m-%d")
                item['summary'] = article.summary
                item['category'] = article.category.name
                item['views'] = article.views
                item['comment_number'] = article.get_comment_number()
                item['img_link'] = article.img_link
                result['msg'].append(item)
            return JsonResponse(result)

        articles = articles[0:5]
        return render(request, 'blog/index.html', locals())



class  Article(View):
    def get(self, request):
        title = '辉哥哥的文章'
        aid = request.GET.get('aid')
        if not aid:
            return redirect('/')
        article = Articles.objects.filter(pk=aid).first()
        if article.is_delete:
            return redirect('/')
        if not request.user.is_superuser:
            article.views+=1
        article.save()
        return render(request, 'blog/article.html', locals())


class CategoryArticle(View):
    def get(self, request, cname):
        title = '分类页面'
        articles = Articles.objects.filter(is_delete=False).filter(category__name=cname)
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
        # path = '/static/test.xlsx'
        # return redirect(path)
        # user = request.user
        # mag = request.user.is_superuser
        agent = request.META.get('HTTP_USER_AGENT', None)
        data = judge_pc_or_mobile(agent)
        # cache.clear()
        return HttpResponse(data)


class DingDing(View):
    def get(self, request):
        title = '海乐园'
        session = Session()
        result = session.query(caiwu).all()
        data = [item.atitle for item in result]
        agent = request.META.get('HTTP_USER_AGENT', None)
        agent = judge_pc_or_mobile(agent)
        return render(request, 'blog/dingding.html', locals())

class DingUser(View):
    def get(self, request):
        code = request.GET.get('code')
        corpid = 'dingee782ddde4ad479035c2f4657eb6378f'
        corpsecret = '8ggjhU52mXi9p1GaEXPbwEy9zW55m8vq_wRONOfcxB06BzelSBiruC37AFeP-uvY'
        access_token = get_dingding_json_data('https://oapi.dingtalk.com/gettoken?corpid={}&corpsecret={}'.format(corpid, corpsecret))['access_token']
        url = 'https://oapi.dingtalk.com/user/getuserinfo?access_token={}&code={}'.format(access_token, code)
        userid = get_dingding_json_data(url)['userid']
        url = 'https://oapi.dingtalk.com/user/get?access_token={}&userid={}'.format(access_token, userid)
        result = get_dingding_json_data(url)

        session = Session()
        ding_user = session.query(dinguser).filter_by(mobile=str(result['mobile'])).first()
        if ding_user is None:
            user = dinguser(name=result['name'],mobile=result['mobile'])
            session.add(user)
            session.commit()
            session.close()
            ding_user = session.query(dinguser).filter_by(mobile=result['mobile']).first()
            print ding_user

        ding_user_id = ding_user.id
        data = {
            'ding_user_id' : ding_user_id
        }

        return JsonResponse(data)

# class DingConfig(View):
#     def get(self, request):
#         corpid = 'dingee782ddde4ad479035c2f4657eb6378f'
#         corpsecret = '8ggjhU52mXi9p1GaEXPbwEy9zW55m8vq_wRONOfcxB06BzelSBiruC37AFeP-uvY'
#         access_token = \
#             get_dingding_json_data(
#                 'https://oapi.dingtalk.com/gettoken?corpid={}&corpsecret={}'.format(corpid, corpsecret))[
#                 'access_token']
#         url = 'https://oapi.dingtalk.com/get_jsapi_ticket?access_token={}'.format(access_token)
#         ticket = get_dingding_json_data(url)['ticket']
#         agentId = '170790877'
#         corpId = 'dingee782ddde4ad479035c2f4657eb6378f'
#         timeStamp = str(int(time.time()))
#         nonceStr = ''.join(str(uuid.uuid4()).split('-'))
#         url = 'https://good-person.cn/blog/dingding/'
#         signature = get_signature(ticket, url, timeStamp, nonceStr)
#         data = {
#             'agentId':agentId,
#             'corpId':corpId,
#             'timeStamp':timeStamp,
#             'nonceStr':nonceStr,
#             'signature':signature
#         }
#         return JsonResponse(data)