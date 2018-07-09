from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$', register_views),
    url(r'^deal', deal_views),
    url(r'^del', del_views),
    url(r'^login/$', login_views),
    url(r'^publish/$', publish_views, name='publishPage'),
    url(r'^main/$', mainpage_views, name='mainPage'),
    url(r'^detail/', detail_views),
    url(r'^$', mainpage_views),
]
