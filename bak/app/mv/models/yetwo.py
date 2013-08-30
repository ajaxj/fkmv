# -*- coding:utf-8
from bak.app.mv.extensions import  db

class YetwoCategory(db.Model):
    __tablename__ = 'yetwocategory'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(45))

class YetwoMovie(db.Model):
    __tablename__ = 'mv_movie_yetwo'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(200))
    img = db.Column(db.String(200))
    category = db.Column(db.String(50))








