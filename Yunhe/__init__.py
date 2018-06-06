#!usr/bin/env python
# coding:utf-8


from flask import Blueprint

from log import log_basic

Yunhe = Blueprint('Yunhe',__name__,template_folder='templates',static_folder='static')
Yunhe_log = log_basic(name='Yunhe')


from . import view