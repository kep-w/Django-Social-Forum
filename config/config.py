import gevent.monkey
import multiprocessing

gevent.monkey.patch_all()

# 监听接口绑定
bind = '0.0.0.1:8000'
preload_app = True
# 日志配置
loglevel = 'error'
logfile = 'log/gunicorn/debug.log'
accesslog = 'log/gunicorn/access.log'
access_log_format = '%(h)s %(t)s %(U)s %(q)s'
errorlog = 'log/gunicorn/error.log'
# 进程名
proc_name = 'vservice'
# 进程id储存文件：专门储存gunicorn进程id，方便kill
pidfile = 'log/gunicorn/gunicorn.pid'
# 进程开启数量
workers = multiprocessing.cpu_count() * 2 + 1
# 线程开启数量
threads = multiprocessing.cpu_count() * 2
# 职程运行模式
worker_class = 'gevent'