# -*- coding:utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from myapp import app

class nullpool_SQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(nullpool_SQLAlchemy, self).apply_driver_hacks(app,info,options)
        from sqlalchemy.pool import NullPool
        options['poolclass'] = NullPool
        del options['pool_size']

db = nullpool_SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'zhuzhu_mv'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    cateen = db.Column(db.String(45))
    catecn = db.Column(db.String(45))
    url = db.Column(db.String(200))
    title = db.Column(db.String(100))
    banben = db.Column(db.String(45))
    arts = db.Column(db.String(200))
    lang = db.Column(db.String(45))
    location = db.Column(db.String(45))
    pubdate = db.Column(db.String(45))
    content = db.Column(db.Text())
    list = db.Column(db.Text())
    status = db.Column(db.Integer)
    img = db.Column(db.String(255))
    pubyear = db.Column(db.String(100))


    def __unicode__(self):
        return self.title

class MovieList(db.Model):
    __tablename__ = 'zhuzhu_ls'
    id = db.Column(db.Integer,primary_key=True)
    mvid = db.Column(db.Integer)
    txt = db.Column(db.String(45))
    res = db.Column(db.Text())
    url = db.Column(db.String(100))

    def __unicode__(self):
        return self.txt

#hakuzy model
class Hahuzy_mv(db.Model):
    __tablename__ = "hakuzy_mv"
    id = db.Column(db.Integer,primary_key=True)
    cateen = db.Column(db.String(45))
    catecn = db.Column(db.String(45))
    url = db.Column(db.String(200))
    title = db.Column(db.String(100))
    banben = db.Column(db.String(45))
    arts = db.Column(db.String(200))
    lang = db.Column(db.String(45))
    location = db.Column(db.String(45))
    pubdate = db.Column(db.String(45))
    content = db.Column(db.Text)
    list = db.Column(db.Text)
    status = db.Column(db.Integer)
    img = db.Column(db.String(255))
    pubyear = db.Column(db.String(45))
    dc = db.Column(db.String(100))

    def __unicode__(self):
        return self.title

#guobianyu.com 模型
class Guobianyu_mv(db.Model):
    __tablename__ = "guobianyu_mv"
    id = db.Column(db.Integer,primary_key=True)
    cateen = db.Column(db.String(45))
    catecn = db.Column(db.String(45))
    url = db.Column(db.String(200))
    title = db.Column(db.String(100))
    banben = db.Column(db.String(45))
    arts = db.Column(db.String(200))
    lang = db.Column(db.String(45))
    location = db.Column(db.String(45))
    pubdate = db.Column(db.String(45))
    content = db.Column(db.Text)
    list = db.Column(db.Text)
    status = db.Column(db.Integer)
    img = db.Column(db.String(255))
    pubyear = db.Column(db.String(45))
    dc = db.Column(db.String(100))

    def __unicode__(self):
        return self.title










