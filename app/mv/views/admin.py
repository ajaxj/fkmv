# -*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
from flask import Module,request,redirect,json, render_template
from app.mv.extensions import db
from app.mv.models.hakuzy import HakuzyMovie,HakuzyMovieCategory

admin = Module(__name__)

@admin.route("/")
def index():
    return render_template('admin/index.html')



#分类列表
@admin.route('/hakuzycatlist')
def hakuzycatlist():
    print HakuzyMovieCategory.query.countnum()
    _catelist = HakuzyMovieCategory.query.all()
    return render_template('admin/hakuzycatlist.html',catelist = _catelist)


@admin.route('/hakuzysearch',methods=('GET','POST'))
def hakuzysearch():
    if request.method == "POST":
       _title = request.form['title']
       _mv = HakuzyMovie.query.get_by_title(_title)

       print _title
       return render_template("admin/hakuzysearch.html",mv = _mv)
    else:
       return render_template("admin/hakuzysearch.html",mv = None)



# @admin.route('/hakuzylist',methods=('GET','POST'))
# def hakuzylist():
#     if request.method == 'POST':
#         # 支付模糊查询
#         _title =  request.form['title']
#         _hakuzylist = Hakuzy.query.filter(Hakuzy.title.like('%'+_title+'%')).all()
#         return render_template('admin/hakuzylist.html',hakuzylist = _hakuzylist)
#     else:
#         _hakuzylist  = Hakuzy.query.limit(10).all()
#         return render_template('admin/hakuzylist.html',hakuzylist=_hakuzylist)


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

