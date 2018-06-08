# coding:utf-8

import os
from flask import Flask
from flask import Blueprint, render_template, abort, jsonify, request,current_app
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.wsgi import DispatcherMiddleware

import config
from log import log_basic
from Yunhe import Yunhe
from Blog import Blog


log_test = log_basic(name='mian')
app = Flask(__name__)
db = SQLAlchemy(app)
CSRFProtect(app)
login_manager = LoginManager(app)
app.register_blueprint(Yunhe)#url_prefix='/yunhe' 给本项目设置默认地址
app.register_blueprint(Blog)
app.config.from_object(config.db_sql)
app.config.from_object(config.basic_conf)





@app.route('/')
def hello_world():
	log_test.info.info('这是一个测试')
	return 'Hello World!'

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
	log_test.info.info('这是一个测试')
	return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
	app.run(port = 5250, debug = True)
