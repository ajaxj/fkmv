# -*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
from flask import Module,Response,Request,json, render_template
from app.mv.extensions import db
from app.mv.models.hakuzy import HakuzyMovie,HakuzyMovieCategory

admin = Module(__name__)

@admin.route("/")
def index():
    return render_template('admin/index.html')



#分类列表
@admin.route('/hakuzycatlist')
def hakuzycatlist():
    _catelist = HakuzyMovieCategory.query.all()
    return render_template('admin/hakuzycatlist.html',catelist = _catelist)


#取出最新十部
@admin.route('/hakuzymovies')
def hakuzymovies():
    # movie = HakuzyMovie.query.first()
    # 动作片
    movies = HakuzyMovie.query.filter_by(category='动作片').limit(3).all()
    return render_template('admin/hakuzymovies.html', movies= movies)


@admin.route('/hakuzyuplist/<id>/')
def hakuzyuplist(id):
    mv = HakuzyMovie.query.get(int(id))
    soup = BeautifulSoup(mv.lists)
    alist = soup.findAll('a')
    _urltxt =alist[0].text
    mv.urltxt = _urltxt
    db.session.add(mv)
    db.session.commit()
    return "ok"

