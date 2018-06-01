#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import logging
from logging import handlers

from config import conf_dir

standard_format = logging.Formatter('%(asctime)s-%(name)s %(pathname)s/%(filename)s[line:%(lineno)d] : %(process)d-%(thread)d-%(module)s-%(funcName)s : %(message)s')

conf_dir = os.path.join(conf_dir,'log')
info = os.path.join(conf_dir,'info.log')
erro = os.path.join(conf_dir,'erro.log')
debug = os.path.join(conf_dir,'debug.log')
critical = os.path.join(conf_dir,'critical.log')

log_dict = {}

def catch_log(cls):
	def fun(name = 'unknow',*args,**kwargs):
		if name not in log_dict:
			log_dict[name] = cls(name, *args, **kwargs)
		return log_dict[name]
	return fun


def closeLogger(name):
	if name in log_dict:
		del log_dict[name]


@catch_log
class log_basic(object):

	def __init__(self,name = 'tt'):
		name = name
		self.info = logging.Logger(name)
		self.info.setLevel(logging.INFO)
		infoHandler = handlers.TimedRotatingFileHandler(info, 'MIDNIGHT', 1, 1)
		infoHandler.setFormatter(standard_format)
		self.info.addHandler(infoHandler)

		self.error = logging.Logger(name)
		self.error.setLevel(logging.INFO)
		infoHandler = handlers.TimedRotatingFileHandler(erro, 'MIDNIGHT', 1, 1)
		infoHandler.setFormatter(standard_format)
		self.error.addHandler(infoHandler)

		self.debug = logging.Logger(name)
		self.debug.setLevel(logging.INFO)
		infoHandler = handlers.TimedRotatingFileHandler(debug, 'MIDNIGHT', 1, 1)
		infoHandler.setFormatter(standard_format)
		self.debug.addHandler(infoHandler)

		self.critical = logging.Logger(name)
		self.critical.setLevel(logging.INFO)
		infoHandler = handlers.TimedRotatingFileHandler(critical, 'MIDNIGHT', 1, 1)
		infoHandler.setFormatter(standard_format)
		self.critical.addHandler(infoHandler)

