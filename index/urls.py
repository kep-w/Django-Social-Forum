from django.conf.urls import url
from django.views import static
from django.conf import settings
from .views import *


urlpatterns = [
    url(r'^register/$', register_views, name='register'),
    url(r'^deal', deal_views),
    url(r'^del', del_views),
    url(r'^login/$', login_views, name='login'),
    url(r'^publish/$', publish_views, name='publishPage'),
    url(r'^detail/$', detail_views, name='detail'),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATICFILES_DIRS}, name='static'),
]
handler404 = page_not_found