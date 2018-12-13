from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^bysj/$', Bysj.as_view(), name='bysj'),
    url(r'^cqc/$', Cqc.as_view(), name='cqc'),
    url(r'^programme/$', Programme.as_view(), name='programme'),
    url(r'^areas/$', Areas.as_view(), name='areas'),
    url(r'^caiwu/$', Caiwu.as_view(), name='caiwu'),
    url(r'^addcaiwu/$', AddCaiwu.as_view(), name='addcaiwu'),
]

