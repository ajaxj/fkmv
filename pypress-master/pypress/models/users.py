#!/usr/bin/env python
#coding=utf-8
from datetime import datetime

from flask.ext.sqlalchemy import BaseQuery

from pypress.extensions import db, cache

class UserQuery(BaseQuery):
    def from_identity(self,identity):
        pass


class User(db.Model):
    __tablename__ = "users"
    #TODO query_class

    #常量
    PER_PAGE = 50
    TWEET_PER_PAGE = 30

    MEMBER = 100
    MODERATOR = 200
    ADMIN = 200

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(100),unique=True,nullable=False)
    _password = db.Column("password",db.String(80),nullable=False)
    role = db.Column(db.Integer,default=MEMBER)
    activation_key = db.Column(db.String(40))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    last_login = db.Column(db.DateTime,default=datetime.utcnow)
    last_request = db.Column(db.DateTime,default=datetime.utcnow)
    block = db.Column(db.Boolean,default=False)

    def __init__(self,*args,**kwargs):
        super(User,self).__init__(*args,**kwargs)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return "<%s>" % self

    #TODO A



class UserCode(db.Model):
    __tablename__ = "usercode"
    id = db.Column(db.Integer,primary_key=True)
    code = db.Column(db.String(20),nullable=True)
    role = db.Column(db.Integer,default=User.MEMBER)

    def __init__(self,*args,**kwargs):
        super(UserCode,self).__init__(*args,**kwargs)

    def __str__(self):
        return self.code

    def __repr__(self):
        return "<%s>" % self


class Twitter(db.Model):
    __tablename__ = 'twitter'
    id = db.Column(db.Integer,primary_key=True)
    token = db.Column(db.String(50))
    #TODO A