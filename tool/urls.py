from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^bysj/$', Bysj.as_view(), name='bysj'),
]

