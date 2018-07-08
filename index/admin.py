from django.contrib import admin
from .models import *

# 将数据库表注册, 可admin登录管理
# Register your models here.
admin.site.register(Users)
admin.site.register(User_Info)
admin.site.register(Message)
admin.site.register(Collection)
admin.site.register(Transpond)
admin.site.register(Comment)
