# coding=utf8

from django.conf.urls import url
from views import *

urlpatterns=[
    url(r'^add/$', AddComment.as_view(), name="addcomment"),
    url(r'^addreply/$', AddReply.as_view(), name='addreply'),
    url(r'^get_reply/$', GetReply.as_view(), name='get_reply'),
]