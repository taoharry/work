#!usr/bin/env python
# coding:utf-8


from EasyWork import db
from datetime import datetime
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = "role"

    #角色设定有三个一个管理员,一个注册用户,一个是匿名用户
    id = db.Column(db.Integer,primary_key=True)
    roles = db.Column(db.String(20),unique=True)

    users =db.relationship("User",backref="role")

    def __unicode__(self):
        return self.roles

class User(UserMixin,db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    passwd  = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.INTEGER,unique=True)

    role_id = db.Column(db.Integer,db.ForeignKey("role.id"))
    article = db.relationship("Article",backref="user")

    def __unicode__(self):
        return self.username



class Article(db.Model):
    # 文章
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    datetm = db.Column(db.DateTime, default=datetime.utcnow())

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    comment = db.relationship("Comment", backref="article")

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __unicode__(self):
        return self.title

class Comment(db.Model):
    # 评论
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Text, nullable=False)
    datetm = db.Column(db.DateTime, default=datetime.utcnow())

    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))

    def __init__(self, comments, article_id):
        self.comments = comments
        self.article_id = article_id

    def __unicode__(self):
        return self.comments


