#  -*- coding:utf-8 -*-
from app.mv.extensions import db

# 正式分类表
class Movcat(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ename = db.Column(db.String(45))
    name = db.Column(db.String(45))


    def __init__(self, ename=None,name=None):
    	self.ename = ename
    	self.name = name


    def __repr__(self):
    	return '<Category %r>' % self.name + self.ename


class Mov(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    banben = db.Column(db.String(50))
    arts = db.Column(db.String(200))
    dc = db.Column(db.String(100))
    lang = db.Column(db.String(50))
    location = db.Column(db.String(50))
    pubdate = db.Column(db.String(50))
    status = db.Column(db.String(50))
    year = db.Column(db.String(50))
    content = db.Column(db.Text)
    img = db.Column(db.String(200))
    fromto = db.Column(db.String(20))
    category_id = db.Column(db.Integer,db.ForeignKey('movcat.id'))
    category = db.relationship('Movcat',backref=db.backref('movs',lazy='dynamic'))


    # def __init__(self, title):
    # 	self.title = title
    #
    # def __repr__(self):
    # 	return '<Mov %r>' % self.title


#明细
class Movdetail(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tp = db.Column(db.Integer)              #属于哪个版本
    url = db.Column(db.String(255))
    mov_id = db.Column(db.Integer,db.ForeignKey('mov.id'))
    movie = db.relationship('Mov',backref=db.backref('movs',lazy='dynamic'))










