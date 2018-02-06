# coding=utf8

from django.conf.urls import url
from views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^index/$', cache_page(3600)(Index.as_view()), name='index'),
    url(r'^article/(?P<aid>\d+)$', Article.as_view(), name='article'),
    url(r'^carticle/(?P<cname>\w+)$', cache_page(3600)(CategoryArticle.as_view()), name='carticle'),
    url(r'^tarticle/(?P<tname>\w+)$', cache_page(3600)(TagArticle.as_view()), name='tarticle'),
]
