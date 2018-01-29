# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.http import JsonResponse


from usercenter.forms import RegisterForm, LoginForm
from blog.models import UserProfile


class Register(View):
    def get(self, request):
        return render(request, "usercenter/register.html")

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            user = UserProfile.objects.filter(username=username).first()
            if user:
                err_allow = u"用户名已经存在"
                return render(request, "usercenter/register.html", locals())
            else:
                user = UserProfile()
                user.username = username
                user.password = make_password(register_form.cleaned_data["password1"])
                user.email = register_form.cleaned_data["email"]
                user.gender = 0
                user.save()
                login(request, user)
                return redirect(reverse("blog:index"))
        else:
            return render(request, "usercenter/register.html", locals())


class Login(View):
    def get(self, request):
        return render(request, "usercenter/login.html")

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(**login_form.cleaned_data)
            if user:
                login(request, user)
                return redirect(reverse("blog:index"))
            else:
                err = u"用户名或密码错误"
                return render(request, "usercenter/login.html", locals())
        else:
            return render(request, "usercenter/login.html", locals())

class CheckUsername(View):
    def get(self, request):
        username = request.GET.get("username")
        count = UserProfile.objects.filter(username=username).count()
        return JsonResponse({"count": count})

class UpdatePwd(View):
    pass