# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

class Bysj(View):
    def get(self, request):
        return render(request, 'tool/bysj.html')
