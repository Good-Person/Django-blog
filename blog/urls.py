# coding=utf8

from django.conf.urls import url
from views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^index/$', Index.as_view(), name='index'),
    url(r'^article/$', Article.as_view(), name='article'),
    url(r'^carticle/(?P<cname>\w+)$', CategoryArticle.as_view(), name='carticle'),
    url(r'^tarticle/(?P<tname>\w+)$', TagArticle.as_view(), name='tarticle'),
    url(r'^test/$', Test.as_view()),
    url(r'^dingding/$', DingDing.as_view(), name='dingding'),
    url(r'^dinguser/$', DingUser.as_view()),
]
