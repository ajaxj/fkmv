# -*- coding:utf-8 -*-

from BeautifulSoup import BeautifulSoup
from flask import Module,request, render_template
from bak.app.mv.extensions import db
from bak.app.mv.models.hakuzy import HakuzyMovie,HakuzyMovieCategory
from bak.app.mv.models.yetwo import YetwoCategory,YetwoMovie
from bak.app.mv.models.mov import Movcat,Mov,Movdetail
from bak.app.mv.forms.yetwoform import YetwoCategoryForm
from bak.app.mv.forms.admin import AdminForm
from bak.app.mv.views.utils import Utils

admin = Module(__name__)

@admin.route("/")
def index():
    # if session.get('logined') == True:
    #     return render_template('admin/index.html.bak')
    # else:
    #     return redirect(url_for('login'))
    return render_template('admin/index.html.bak')

@admin.route('/login',methods=['GET','POST'])
def login():
    form = AdminForm()
    return render_template('admin/login.html',form=form)



# **********************  正式mov ***************

#所有分类
@admin.route('/categorylist')
def categorylist():
    _categorylist = Movcat.query.all()
    return render_template('admin/categorylist.html',categorylist = _categorylist)

@admin.route('/movielist')
def movielist():
    _movielist = Mov.query.all()
    return render_template('admin/movielist.html',movielist = _movielist)

@admin.route('/moviedetail')
def moviedetail():
    #TODO 补充根据MVID查找
    _moviedetail_list = Movdetail.query.all()
    return render_template('admin/moviedetail.html',moviedetail_list = _moviedetail_list)




#初始数据
@admin.route('/initdata')
def initdata():
    cat1 = Movcat("dongzhuo","分类1")

    mv1 = Mov()
    mv1.title = "title1"
    mv1.banben = "banben1"
    mv1.arts = "arts1"
    mv1.dc = "dc1"
    mv1.lang = "lang1"
    mv1.location = "location1"
    mv1.pubdate = "pubdate1"
    mv1.statue = "status1"
    mv1.content = "content1"
    mv1.img = "img1"
    mv1.fromto = "hakuzy"
    mv1.category = cat1

    mv2 = Mov()
    mv2.title = "title2"
    mv2.banben = "banben2"
    mv2.arts = "arts2"
    mv2.dc = "dc2"
    mv2.lang = "lang2"
    mv2.location = "location2"
    mv2.pubdate = "pubdate2"
    mv2.statue = "status2"
    mv2.content = "content2"
    mv2.img = "img2"
    mv2.fromto = "hakuzy"
    mv2.category = cat1

    md1 = Movdetail()
    md1.tp = 1
    md1.url = "url1"
    md1.movie = mv1

    md2 = Movdetail()
    md2.tp = 1
    md2.url = "url2"
    md2.movie = mv1

    md3 = Movdetail()
    md3.tp = 1
    md3.url = "url1"
    md3.movie = mv2

    db.session.add(cat1)
    db.session.add(mv1)
    db.session.add(mv2)
    db.session.add(md1)
    db.session.add(md2)
    db.session.add(md3)
    db.session.commit()








    return "init data ok"






# ********************* yetwo ***************


#只取十条

@admin.route('/yetwocatlist')
def yetwocatlist():
    _catelist = YetwoCategory.query.all()
    return render_template('admin/yetwocatlist.html',catelist= _catelist)


@admin.route('/yetwomovies10')
def yetwolist():
    _mvs = YetwoMovie.query.limit(10).all()
    return render_template('admin/yetwomovies10.html',mvs=_mvs)


@admin.route('/addyetwocategory')
def addyetwocategory():
    form = YetwoCategoryForm()
    return render_template('admin/addyetwocategory.html',form=form)



#分类列表
@admin.route('/hakuzycatlist')
def hakuzycatlist():
    print HakuzyMovieCategory.query.countnum()
    _catelist = HakuzyMovieCategory.query.all()
    return render_template('admin/hakuzycatlist.html',catelist = _catelist)

#取出十个
@admin.route('/hakuzymovies10/<category>')
def hakuzymovies10(category):
    _mvs = HakuzyMovie.query.get_limit10_desc(category)
    return render_template('admin/hakuzymovies10.html',movies = _mvs)


# 读取详细url更新数据到发布mov里面
@admin.route('/hakuzymov/<id>')
def hakuzyUpToMov(id):
    _mv = HakuzyMovie.query.get(id)
    _url =  "http://www.hakuzy.com" + _mv.url
    myutils = Utils()
    list = myutils.fetchHakuzyDetail(_url)
    #list = [_title,_banben,_arts,_dc,_category,_lang,_location,_pubdate,_status,_year,_content]
    mv= Mov()
    mv.title = list[0]
    mv.banben = list[1]
    mv.arts = list[2]
    mv.dc = list[3]
    mv.catestr = list[4]
    mv.lang = list[5]
    mv.location = list[6]
    mv.pubdate = list[7]
    mv.status = list[8]
    mv.year = list[9]
    mv.content = list[10]
    mv.fromto = 'hakuzy'
    db.session.add(mv)
    db.session.commit()



    return "http://www.hakuzy.com" + _mv.url








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
#         return render_template('admin/hakuzylist.html.bak',hakuzylist = _hakuzylist)
#     else:
#         _hakuzylist  = Hakuzy.query.limit(10).all()
#         return render_template('admin/hakuzylist.html.bak',hakuzylist=_hakuzylist)




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



