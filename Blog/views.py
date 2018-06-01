#!usr/bin/env python
# coding:utf-8


from flask import render_template, request, jsonify,Response


from Blog import Blog

@Blog.route('/blog',methods=['GET'])
def index():
	return "Blog index"