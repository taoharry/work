# coding:utf-8

import os
from flask import Flask
from flask import Blueprint, render_template, abort, jsonify, request,current_app
from flask_wtf import Form

from log import log_basic
from Yunhe import Yunhe
from Blog import Blog

print os.getcwd()
app = Flask(__name__)
app.register_blueprint(Yunhe)
app.register_blueprint(Blog)
with app.app_context():
	print current_app.name

log_test = log_basic(name='mian')
log_test.info.info('这')



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
