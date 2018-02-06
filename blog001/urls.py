from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^comment/', include('comment.urls', namespace='comment')),
    url(r'usercenter/', include('usercenter.urls', namespace='usercenter')),
    url(r'^search/', include('haystack.urls')),
    url(r'^$', cache_page(3600)(views.Index.as_view())),
]
