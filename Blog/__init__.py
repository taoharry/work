#!usr/bin/env python
# coding:utf-8

from flask import Blueprint


Blog = Blueprint('Blog',__name__,template_folder='tempaltes',static_folder='static')


from . import views,model
from EasyWork import db

db.create_all()



