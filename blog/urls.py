# coding=utf8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.Index.as_view(), name='index'),
    url(r'^article/(?P<aid>\d+)$', views.Article.as_view(), name='article'),
]
