# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-07 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_time', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '点赞列表',
                'verbose_name_plural': '点赞列表',
                'db_table': 'collection',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, null=True)),
                ('comment_time', models.DateTimeField(auto_now=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '评论列表',
                'verbose_name_plural': '评论列表',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('picture', models.ImageField(null=True, upload_to='images/msgPicture')),
                ('public_time', models.DateTimeField(auto_now=True)),
                ('collect_num', models.IntegerField(null=True)),
                ('agree_num', models.IntegerField(null=True)),
                ('comment_num', models.IntegerField(null=True)),
                ('transpond_num', models.IntegerField(null=True)),
                ('read_num', models.IntegerField(null=True)),
                ('label', models.CharField(max_length=50, null=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '微博消息',
                'verbose_name_plural': '微博消息',
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='Transpond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transpond_time', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Message')),
            ],
            options={
                'verbose_name': '转发列表',
                'verbose_name_plural': '转发列表',
                'db_table': 'relation',
            },
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default=None, null=True, upload_to='images/avatar')),
                ('realname', models.CharField(max_length=30, null=True, unique=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('sex', models.IntegerField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('intro', models.CharField(max_length=200, null=True)),
                ('blogurl', models.URLField(null=True)),
            ],
            options={
                'verbose_name': '用户详细信息',
                'verbose_name_plural': '用户详细信息',
                'db_table': 'info',
            },
        ),
        migrations.CreateModel(
            name='UserLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '用户标签表',
                'verbose_name_plural': '用户标签表',
                'db_table': 'userlabel',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('signup_time', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='userlabel',
            name='users',
            field=models.ManyToManyField(to='index.Users'),
        ),
        migrations.AddField(
            model_name='user_info',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users'),
        ),
        migrations.AddField(
            model_name='transpond',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users'),
        ),
        migrations.AddField(
            model_name='message',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users'),
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Message'),
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users'),
        ),
        migrations.AddField(
            model_name='collection',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Message'),
        ),
        migrations.AddField(
            model_name='collection',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users'),
        ),
    ]
