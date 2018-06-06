#!usr/bin/env python
# coding:utf-8


from flask import request,redirect,render_template,url_for,session,flash
from model import User,Role,Article,Comment
from flask_login import login_required,login_user

from EasyWork import db,login_manager
from Blog import Blog
from blog_form import RegistForm
from utils.check import check_password
from utils.page import all_page,page_list


@login_manager.user_loader
def load_user(userid):
	return User.query.get(userid)

@Blog.route('/register',methods=['GET','POST'])
def registers():
	form = RegistForm()
	if request.method == "GET":
		return render_template("register.html",form=form)
	else:
		form = RegistForm(request.form)
		print form.csrf_token.data
		if form.validate():
			username = form.username.data
			user = User.query.filter_by(username=username).first()
			if user != None:flash('该用户已经注册')
			password = check_password().set_password(form.passwd.data)
			phone = form.phone.data
			email = form.email.data
			if username == 'admin':
				role_id = 1
			else:
				role_id = 2
			new_user = User(username=username,passwd=password,phone=phone,email=email,role_id=role_id)
			db.session.add(new_user)
			db.session.commit()
			flash('Register sucess')
			return redirect(url_for('Blog.login'))
		else:
			flash('输入不符合规定')
			return render_template("register.html",form=form)

@Blog.route("/login", methods=["POST","GET"])
def login():
	form = RegistForm()
	if request.method == "GET":
		return render_template("login.html",form=form)
	else:
		username = request.form.get("username")
		passwd = request.form.get("passwd")
		pass_url = User.query.filter_by(username=username).first()
		if pass_url == None:
			flash("NO USER")
			return render_template("login.html")
		if check_password().verify_password(pass_url.passwd,passwd):
			load_user(int(pass_url.id))
			flash('Logged in successfully.')
			login_user(pass_url,remember=True)
			next = request.args.get('next')
			return redirect(next or url_for('Blog.index'))
		return render_template("login.html",form=form)

@Blog.route("/blog", methods=["POST","GET"])
def index():
	if request.method == "POST":
		title = request.form.get("search")
		all = Article.query.filter(Article.title.like(title)).all()
	else:
		all = Article.query.all()
		longer = len(all)
	if not all:render_template('blog_basic.html',massage = '暂无文章')
	allpage = all_page(longer, 5)
	page = request.args.get('page',1)
	if not isinstance(page,[int,float]): page = 1
	arg = abs(int(page))
	if arg > allpage:arg = 1
	page = page_list(allpage, arg)
	# all = shut_page_content(arg, all)
	show = all[(arg-1)*20:arg*20]
	return render_template("index.html", show_content=show, page_number=page)

@Blog.route('/blog/write')
@login_required
def write_aritle():
	user = session.get("user_id",'')
	if request.method=="GET":
		if not user  and User.query.filter_by(username=user):
			print "this is write save session %s"%session.get("user")
			return render_template("write.html")
		else:
			return redirect(url_for('Blog.login'))
	#这里存入应该是带有html标签的内容以便存储信息
	if request.method =="POST" :
		t = request.form.get("title")
		con = request.form.get("content")
		title = Article(title=t,content=con,user_id=user)
		try:
			db.session.add(title)
			db.session.commit()
		except Exception as e:
			return erro(e)
		return redirect(url_for("Blog.index"))

@Blog.route("/blog/look/<int:id>" ,methods=["GET","POST"])
def look_title(id):

	aritle = Article.query.filter_by(id=id).first()
	title = aritle.title
	content = aritle.content

	p = Comment.query.filter_by(article_id=id).all()

	if request.method =="POST":
		_commit = request.form.get("cont")
		print "this is commit %s"%_commit

		commit_Comment = Comment(comments=_commit,article_id=id)
		try:
			db.session.add(commit_Comment)
			db.session.commit()
		except Exception as e:
			return redirect(url_for("main.e"))

	return render_template("looktitle.html",title=title,content=content,discuss=p,name=id)

@Blog.route('/logout')
@login_required
def logout():
	# remove the username from the session if it is there

	session.pop('user', None)
	return redirect(url_for('main.index'))


def erro(*args,**kwargs):
	return """
			<h1>wrong wrong wrong wrong wrong</h1>
			
			"""