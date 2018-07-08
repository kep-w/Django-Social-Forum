from django.db import models


# 用户表
class Users(models.Model):
    uname = models.CharField(max_length=30)
    pwd = models.CharField(max_length=40)
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    signup_time = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 用户详细信息表
class User_Info(models.Model):
    users = models.ForeignKey(Users)
    avatar = models.ImageField(upload_to='images/avatar', default=None, null=True)
    realname = models.CharField(max_length=30, null=True, unique=True)
    address = models.CharField(max_length=100, null=True)
    sex = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    intro = models.CharField(max_length=200, null=True)
    blogurl = models.URLField(null=True)

    def __str__(self):
        return self.users.get('uname', None)

    class Meta:
        db_table = 'info'
        verbose_name = '用户详细信息'
        verbose_name_plural = verbose_name


# 用户个人标签表
class UserLabel(models.Model):
    label = models.CharField(max_length=50)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'userlabel'
        verbose_name = '用户标签表'
        verbose_name_plural = verbose_name


# 用户发布微博表
class Message(models.Model):
    users = models.ForeignKey(Users)
    content = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='images/msgPicture', null=True)
    public_time = models.DateTimeField(auto_now=True)
    collect_num = models.IntegerField(null=True)
    agree_num = models.IntegerField(null=True)
    comment_num = models.IntegerField(null=True)
    transpond_num = models.IntegerField(null=True)
    read_num = models.IntegerField(null=True)
    label = models.CharField(max_length=50, null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.users.uname

    class Meta:
        db_table = 'message'
        verbose_name = '微博消息'
        verbose_name_plural = verbose_name


# 用户评论表
class Comment(models.Model):
    users = models.ForeignKey(Users)
    message = models.ForeignKey(Message)
    content = models.CharField(max_length=100, null=True)
    comment_time = models.DateTimeField(null=True, auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.message.content

    class Meta:
        db_table = 'comment'
        verbose_name = '评论列表'
        verbose_name_plural = verbose_name


# 用户点赞表
class Collection(models.Model):
    users = models.ForeignKey(Users)
    message = models.ForeignKey(Message)
    collect_time = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.users.uname

    class Meta:
        db_table = 'collection'
        verbose_name = '点赞列表'
        verbose_name_plural = verbose_name


# 用户转发表
class Transpond(models.Model):
    users = models.ForeignKey(Users)
    message = models.ForeignKey(Message)
    transpond_time = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.users.uname

    class Meta:
        db_table = 'transpond'
        verbose_name = '转发列表'
        verbose_name_plural = verbose_name
