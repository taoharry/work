#!usr/bin/env python
# coding:utf-8

from flask import Blueprint

#静态文件,static_folder 指定静态文件路径,static_url_path 制定静态文件链接,再在模板中使用跳转链接.否则静态文件指向项目默认static文件
Blog = Blueprint('Blog',__name__,template_folder='templates',static_folder='static',static_url_path='/Blog')


from . import views,model
from EasyWork import db

db.create_all()



