# Django 框架实现社交论坛
- 基于Django框架实现社交论坛功能, 涵盖基本Django框架的功能
- 整个项目用到技术软件/模块如下:

    - Python version 3
    - Django version 1.11.8 
    - MySQL to manage the data
    - hashlib to change the password that user input 
    
- 基本功能如下:
    - 注册: 通过django中的forms模块生成对应输入控件, 获取输入内容判断数据库后存入
    - 登录: 
        * 获取输入内容,验证数据库, 登录成功保存登录状态(session)
        * 设置浏览器关闭删除用户对应的session
    - 首页: 
        * 默认展示首页, 留有登录注册入口. 未登录点击动态下的点赞转发评论都进入登录入口
        * 登录成功, 首页头部加入用户名
        * 展示论坛内的全部动态, 可以点赞, 转发, 评论, 也可以查看详情
    - 发布: 发布个人动态,可以配图, 可以加标签
    - 登出: 点击退出删除登录状态
    - 页面间通过模板的继承减少代码量

- 页面处理上, 通过设置只有匿名请求（即不是由登录的用户）才被缓存, 避免了页面重定向不刷新
    
- 说明:
    - 运行项目需要先加载数据库
        * 使用MySQL创建对应的库命令: create database microblog default charset utf8;
        * ./manage.py makemigrations
        * ./manage.py migrate
    - 运行项目
        * ./manage.py runserver [host:port]  --> []内内容代表可以省略,省略默认访问地址: 127.0.0.1:8000
    - 创建超级管理员
        * ./manage.py createsuperuser
        * 127.0.0.1:8000/admin 可以登录后台进行数据管理

- 线上通过nginx部署环境, 保持项目后台运行, 通过日志记录状态
    * 以通过Nginx 解决Django 单线程的问题 实现高并发需求
    * [项目部署线上访问地址](http://www.pbase.xyz "个人测试")
