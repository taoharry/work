#!usr/bin/env python
# coding:utf-8

from flask import Blueprint

Blog = Blueprint('Blog',__name__,template_folder='./templates',static_folder='./static')


from . import views



