# coding:utf-8
from flask import abort
from flask.ext.sqlalchemy import BaseQuery
from app.mv.extensions import db

__author__ = 'Administrator'

#自定义分类Query
class HakuzyMovieCategoryQuery(BaseQuery):
    def countnum(self):
        return self.count()



#分类
class HakuzyMovieCategory(db.Model):
    __tablename__ = "mv_movie_hakuzycat"

    #绑定自定义QUERY
    query_class = HakuzyMovieCategoryQuery

    id  = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(45))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


#自定义 hakuzymovie query
class HakuzyMovieQuery(BaseQuery):

    #mv总数
    def count_num(self):
        return self.count()


    #通过分类查找最新十个
    def get_limit10(self,category):
        _mvs = self.filter(HakuzyMovie.category ==category).order_by("id desc").limit(10).all()
        if _mvs is None:
            abort(404)
        return _mvs

    #通过标题查询
    def get_by_title(self,title):
        mv = self.filter(HakuzyMovie.title == title).first()
        if mv is None:
            abort(404)
        return mv




class HakuzyMovie(db.Model):
    __tablename__ = "mv_movie_hakuzy"

    query_class = HakuzyMovieQuery

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(200))
    img = db.Column(db.String(200))
    category = db.Column(db.String(50))
    contents = db.Column(db.Text)
    lists = db.Column(db.Text)
    urltxt = db.Column(db.Text)



    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return '<Movie %r>' % self.title




