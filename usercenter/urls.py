# coding=utf8

from django.conf.urls import url
from views import *

urlpatterns=[
    url(r'^register/$', Register.as_view(), name="register"),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^check_username/$', CheckUsername.as_view(), name='check_username'),
    url(r'^update_pwd/$', UpdatePwd.as_view(), name='update_pwd'),
]