# Django 框架实现社交论坛
### 基于Django框架实现社交论坛功能, 涵盖基本Django框架的功能
-整个项目用到技术软件/模块如下:

    -Python version 3
    -Django version 1.11.8 
    -MySQL to manage the data
    -hashlib to change the password that user input 
    
-基本功能如下:
    -注册: 通过django中的forms模块生成对应输入控件, 获取输入内容判断数据库后存入
    -登录: 
        获取输入内容,验证数据库, 登录成功保存登录状态(session)
        设置浏览器关闭删除用户对应的session
    -首页: 
        默认展示首页, 留有登录注册入口. 未登录点击动态下的点赞转发评论都进入登录入口
        登录成功, 首页头部加入用户名
        展示论坛内的全部动态, 可以点赞, 转发, 评论, 也可以查看详情
    -发布: 发布个人动态,可以配图, 可以加标签
    -登出: 点击退出删除登录状态
