from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$', register_views, name='register'),
    url(r'^deal', deal_views),
    url(r'^del', del_views),
    url(r'^login/$', login_views, name='login'),
    url(r'^publish/$', publish_views, name='publishPage'),
    url(r'^detail/$', detail_views, name='detail'),
]