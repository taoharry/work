#!usr/bin/env python
# coding:utf-8

import json
import os,time
import urllib2
from flask import render_template, request, jsonify,Response, url_for

from . import Yunhe



@Yunhe.route('/yunhe')
def test():
	return render_template('index.html')


@Yunhe.route('/dict_tojson',methods=['GET','POST'])
def complie_json():
	if request.method == 'GET':
		return """<form action="/dict_tojson" method="post">
						<input type="text" name="name" placeholder="字典输入">
						<input type="submit" value="Submit" />
					</form>
				"""
	elif request.method == 'POST':
		dt = request.form.get('name')
		if isinstance(dt,str):
			dt = json.loads('dt',encoding='utf8')
		return Response(dt, mimetype='application/json')


@Yunhe.route('/ossdata',methods=['GET',"POST"])
def oss_get_data():
	if request.method == 'GET':
		return """<form action="/ossdata" method="post">
						<input type="text" name="url" placeholder="url">
						<input type="submit" value="Submit" />
					</form>
				"""
	elif request.method == "POST":
		url = request.form.get('url')
		resault = []
		try:
			read = urllib2.urlopen(url).read()
		except:
			raise "Can't get response,please check %s"%url
		r = read.split('\r\n')[0:-1]
		for i in r:
			dt = json.loads(i)
			resault.append(dt)
		return  Response(json.dumps(resault,ensure_ascii=False), mimetype='application/json')

@Yunhe.route('/int_time_str',methods=["POST"])
def time_to_str():
	if request.method == "POST":
		int_time = int(request.form.get('select_int'))
		return render_template('index.html',int_time_resault=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int_time)))

