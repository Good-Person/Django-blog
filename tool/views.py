# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
import json
import time

from models import *

from utils.sqlalcemyTest import Caiwu as caiwu
from utils.sqlalcemyTest import User
from utils.sqlalcemyTest import Data
from utils.sqlalcemyTest import Areas as city
from utils.sqlalcemyTest import Session


class Bysj(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('usercenter:login'))
        parking1 = Parking.objects.all()[0:5]
        parking2 = Parking.objects.all()[5:]
        user_parking = request.user.parking_user.first()
        return render(request, 'tool/bysj01.html', locals())

class Cqc(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('usercenter:login'))
        user_parking = request.user.parking_user.first()
        if user_parking is None:
            parkings = Parking.objects.all().order_by('-id')
            for parking in parkings:
                if parking.is_null:
                    parking_num = parking.id
                    parking.user = request.user
                    parking.is_null = False
                    parking.save()
                    return render(request, 'tool/cqc.html', locals())
        else:
            parking_num = user_parking.id
            user_parking.user = None
            user_parking.is_null = True
            user_parking.save()
        return render(request, 'tool/cqc.html', locals())

class Programme(View):
    def get(self, request):
        parking_num = int(request.GET.get('parking_num'))
        content = MovePark.objects.all().order_by('-id')
        content = content[parking_num - 1].content
        alist = content.split(';')
        data = []
        for item in alist:
            data.append(item.split('-'))
        leng = len(data[0])
        result = {
            'leng':leng,
            'data':data
        }
        return JsonResponse(result)


class Areas(View):
    def get(self, request):
        pid = request.GET.get('pid')
        callback = request.GET.get('callback')
        result = {
            'msg':[]
        }
        session = Session()
        if not pid:
            cityes = session.query(city).filter_by(pid=None).all()
        else:
            cityes = session.query(city).filter_by(pid=pid).all()
        for item in cityes:
            # result.append({'aid':item.id, 'atitle':item.atitle, 'pid':item.pid})
            result['msg'].append('<option value="{}">{}</option>'.format(item.id, item.atitle))

        # return HttpResponse(json.dumps(result), content_type='application/json')
        # return JsonResponse(json.dumps('{}({})'.format(callback, result)))
        return HttpResponse('{}({})'.format(callback, json.dumps(result)))
        # return JsonResponse(result)

class Caiwu(View):
    def get(self, request):
        session = Session()
        result = session.query(caiwu).all()
        data = ''
        for item in result:
            data += item.atitle
        return HttpResponse(data)

class AddCaiwu(View):
    def get(self, request):
        user_id = int(request.GET.get('user_id'))
        title = json.loads(request.GET.get('title'))
        info = json.loads(request.GET.get('ainfo'))

        session = Session()
        user = session.query(User).filter_by(id=user_id).first()
        result = []
        create_time = time.strftime('%Y-%m-%d', time.localtime())
        for i in range(len(title)-1):
            title = session.query(caiwu).filter_by(atitle=title[i]).first()
            result.append(Data(info=info[i], create_time=create_time, user_id=user.id, caiwu_id=title.id))

        session.add_all(result)
        session.commit()
        session.close()

        return JsonResponse({'status':200, 'msg':'数据添加成功'})
