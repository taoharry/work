#!usr/bin/env python
# coding:utf-8

import os
import os

CRITICAL = 'CRITICAL'
ERROR = 'ERROR'
WARNING = 'WARNING'
INFO = 'INFO'
DEBUG = 'DEBUG'

conf_dir = os.path.dirname(os.path.realpath(__file__))
db_dir = os.path.join(conf_dir,'db')

class db_sql(object):
	SQLALCHEMY_DATABASE_URI =  'sqlite:////{}/test.db'.format(db_dir)

class basic_conf(object):
	SECRET_KEY = os.urandom(20)
