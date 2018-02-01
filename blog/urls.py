# coding=utf8

from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^index/$', Index.as_view(), name='index'),
    url(r'^article/(?P<aid>\d+)$', Article.as_view(), name='article'),
    url(r'^carticle/(?P<cname>\w+)$', CategoryArticle.as_view(), name='carticle'),
    url(r'^tarticle/(?P<tname>\w+)$', TagArticle.as_view(), name='tarticle'),
]
