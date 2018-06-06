#!usr/bin/env python
# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Length,EqualTo,InputRequired,Email,NumberRange

class RegistForm(FlaskForm):
	username = StringField('Username',validators=[Length(min=3,max=10,message=u"用户名长度有问题")])
	passwd = StringField('Password',validators=[Length(min=3,max=20,message=u"密码长度有问题")])
	phone = IntegerField('Phone')
	email = StringField('Email',validators=[Email()])

class login(FlaskForm):
	username = StringField('Username', validators=[Length(min=3, max=10, message=u"用户名长度有问题")])
	passwd = StringField('Password', validators=[Length(min=6, max=20)])
