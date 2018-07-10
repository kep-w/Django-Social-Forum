import hashlib
import json
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *

# ajax 请求反馈
ok = json.dumps({'resp': 'ok'})
no = json.dumps({'resp': 'no'})

# 登录处理视图


def login_views(request):
    if request.method == 'GET':
        print('get方式提交')
        form = LoginForm()
        user = request.COOKIES.get('user', None)
        if user:
            request.session['user'] = user
            return HttpResponseRedirect('/')
        else:
            request.session['user'] = None
            return render(request, 'login.html', locals())
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['uname']
            pwd = data['pwd']
            ch = hashlib.md5()
            ch.update(pwd.encode())
            pwd = ch.hexdigest()
            try:
                obj = Users.objects.get(uname=name)
            except Exception as e:
                print(e)
                err = '用户名不存在,请重试!'
                return render(request, 'login.html', locals())
            else:
                if pwd == obj.pwd:
                    request.session['user'] = name
                    resp = HttpResponseRedirect('/')
                    resp.set_cookie('user', name, expires=60 * 60 * 24 * 7)
                    return resp
                else:
                    err = '密码有误, 请重试!'
                    return render(request, 'login.html', locals())
        else:
            err = '输入有误, 请重试'
            print('输入数据无效')
            return render(request, 'login.html', locals())


# 注册处理视图
def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        user = request.COOKIES.get('user', None)
        if user:
            request.session['user'] = user
            resp = HttpResponseRedirect('/')
        else:
            resp = render(request, 'register.html', locals())
        return resp
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['uname']
            try:
                obj = Users.objects.get(uname=name)
            except BaseException:
                pwd = data['pwd']
                ch = hashlib.md5()
                ch.update(pwd.encode())
                data['pwd'] = ch.hexdigest()
                obj = Users(**data)
                obj.save()
                request.session['user'] = name
                resp = HttpResponseRedirect('/')
                resp.set_cookie('user', name, expires=60 * 60 * 24 * 7)
                return resp
        else:
            return render(request, 'register.html', locals())


# 主页处理视图
def mainpage_views(request):
    all_list = messages()
    username = request.COOKIES.get('user', '未登录')
    if not username:
        username = request.session.get('user', '未登录')
        if not username:
            username = '未登录'
    return render(request, 'main.html', locals())


# 详情页处理视图
def detail_views(request):
    if request.method == 'POST':
        global msg_id
        msg_id = request.POST.get('msg_id')
        return HttpResponse(ok)
    else:
        try:
            obj = Message.objects.get(id=msg_id)
            username = request.COOKIES.get('user')
            content = obj.content
            author = obj.users.uname
            public_time = obj.public_time
            coms = Comment.objects.filter(message_id=msg_id)
        except BaseException:
            return HttpResponseRedirect('/')
        else:
            comments = []
            for c in coms:
                d = {}
                d['cauthor'] = c.users.uname
                d['comment_time'] = c.comment_time
                d['content'] = c.content
                comments.insert(0, d)
            if username:
                print(locals())
                return render(request, 'detail.html', locals())
            else:
                username = request.session.get('user', None)
                if username:
                    return render(request, 'detail.html', locals())
                else:
                    return HttpResponseRedirect('/user/login/')


# 点赞转发评论处理视图, 前端通过ajax提交
def deal_views(request):
    atype = request.POST.get('type')
    username = request.POST.get('username')
    msg_id = request.POST.get('msg_id')
    obj = Message.objects.get(id=int(msg_id))
    if atype == 'agree':
        col = Collection.objects.filter(message_id=obj.id, users_id=Users.objects.get(uname=username).id)
        if col:
            return HttpResponse(no)
        else:
            if obj.agree_num:
                obj.agree_num = obj.agree_num + 1
            else:
                obj.agree_num = 1
            adic = {
                'users': Users.objects.get(uname=username),
                'message': obj
            }
            Collection(**adic).save()
            obj.save()
            return HttpResponse(ok)
    if atype == 'transpond':
        if obj.users.uname == username:
            return HttpResponse(no)
        else:
            tran = Transpond.objects.filter(message_id=obj.id, users_id=Users.objects.get(uname=username).id)
            if tran:
                return HttpResponse(no)
            else:
                if Message.objects.filter(content=obj.content, users_id=Users.objects.get(uname=username).id):
                    return HttpResponse(no)
                else:
                    if obj.transpond_num:
                        obj.transpond_num = obj.transpond_num + 1
                    else:
                        obj.transpond_num = 1
                    obj.save()
                    tdic = {
                        'users': Users.objects.get(uname=username),
                        'content': obj.content,
                        'picture': obj.picture,
                        'label': '转发',
                    }
                    Message(**tdic).save()
                    ttdic = {
                        'users': Users.objects.get(uname=username),
                        'message': obj
                    }
                    Transpond(**ttdic).save()
                    return HttpResponse(ok)
    if atype == 'comment':
        cdic = {
            'users': Users.objects.get(uname=username),
            'message': obj,
            'content': request.POST.get('comment_content')
        }
        if obj.comment_num:
            obj.comment_num = obj.comment_num + 1
        else:
            obj.comment_num = 1
        obj.save()
        Comment(**cdic).save()
        return HttpResponse(ok)

# 用户点击退出登录的处理缓存登录状态的视图


def del_views(request):
    atype = request.POST.get('type')
    username = request.POST.get('username')
    if atype == 'delSession':
        resp = HttpResponse({'msg': 'ok'})
        resp.set_cookie('user', '', expires=60 * 60)
        request.session['user'] = None
        return resp


# 发布新微博的处理视图
def publish_views(request):
    if request.method == 'GET':
        username = request.COOKIES.get('user', None)
        if username:
            return render(request, 'publish.html', locals())
        else:
            username = request.session.get('user', None)
            if username:
                return render(request, 'publish.html', locals())
            else:
                return HttpResponseRedirect('/user/login/')
    else:
        user = request.POST.get('user')
        if request.POST.get('mblog'):
            mblog = request.POST.get('mblog').strip()
            label = request.POST.get('label').strip()
            if request.POST.get('path'):
                f = request.FILES['picpath']
                pic = str(time.time()) + user
                with open('static/images/msgPicture/{}'.format(pic), 'wb') as fd:
                    for chunk in f.chunks():
                        fd.write(chunk)
            else:
                pic = None
            dic = {
                'users': Users.objects.get(uname=user),
                'content': mblog,
                'label': label,
                'picture': pic,
            }
            Message(**dic).save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/user/publish/')


# 获取微博列表的方法
def messages():
    all_list = []
    message = Message.objects.all()
    for m in message:
        if m.isActive:
            d = {}
            d['author'] = m.users.uname
            d['id'] = m.id
            d['label'] = m.label
            d['public_time'] = m.public_time
            d['content'] = m.content
            d['picture'] = m.picture
            d['agree_num'] = m.agree_num
            d['transpond_num'] = m.transpond_num
            d['comment_num'] = m.comment_num
            all_list.insert(0, d)
    return all_list
