"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views import static

# 路由配置, 除了admin 其他都分配到index应用的urls处理
from index.views import mainpage_views
from .views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('index.urls')),
    url(r'^$', mainpage_views, name='mainPage'),
    # 配置静态文件的映射
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATICFILES_DIRS}, name='static'),
]


handler403 = page_permission_denied
handler404 = page_not_found
handler500 = page_inter_error
