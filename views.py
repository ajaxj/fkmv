#coding=utf8
from flask import render_template,request, redirect
from flask.ext.paginate import Pagination
import time
#from models.model import Guestbook

from myapp import app
#from blog.views import blog
from admin.views import admin

from models.data_wrapper import DataWrapper
dw = DataWrapper()

#app.register_blueprint(blog,url_prefix="/blog")
app.register_blueprint(admin,url_prefix="/admin")

# -- Error Control --
class ViewError(StandardError):
    def __init__(self, error):
        self.error = error
    def __str__(self):
        return 'ViewError: ' + self.error
#example: raise ViewError('error message')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/error/404')
def error_404():
    return render_template('404.html'), 404

@app.route('/error/500')
def error_500():
    return render_template('500.html'), 500


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detail")
def detail():
    return render_template("detail.html")


@app.route("/itemlist")
def itemlist():
    return render_template("itemlist.html")

@app.route("/player")
def player():
    return render_template("player.html")



# @app.route("/")
# @app.route("/<category>.html")
# def index(category=""):
#     if category == "":
#         _title = u"TV山"
#         _dzmvs = dw.get_movielist_by_cateen_limit('dongzuopian',12)
#         _xjmvs = dw.get_movielist_by_cateen_limit('xijupian',12)
#         _warmvs = dw.get_movielist_by_cateen_limit('zhanzhengpian',12)
#         _khmvs = dw.get_movielist_by_cateen_limit('kehuanpian',12)
#         _aqmvs = dw.get_movielist_by_cateen_limit('aiqingpian',12)
#         _kbmvs = dw.get_movielist_by_cateen_limit('kongbupian',12)
#         _jqmvs = dw.get_movielist_by_cateen_limit('juqingpian',12)
#         return render_template("index.html.bak",title=_title,dzmvs=_dzmvs,xjmvs=_xjmvs,warmvs=_warmvs,khmvs=_khmvs,aqmvs=_aqmvs,kbmvs=_kbmvs,jqmvs=_jqmvs)
#     elif category == "dongzuopian":
#         _title = u"动作片"
#         pagesize = 24 #设定每页显示条目数
#         page = int(request.args.get('page',0)) #获取当前页面页数
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize) #get_MongoData是我自己的函数，根据页数过滤要显示的数据（因为实在太大了）
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page) #total的值是总数据条目，per_page表示每页显示数目，page就是当前页数。还可以设置向前/后页面标签（默认是<</>>）等
#         return render_template("dongzuopian.html",mvs=_mvs,title=_title,pagination=pagination)
#     elif category == "xijupian":
#         _title = u"喜剧片"
#         pagesize = 24
#         page = int(request.args.get('page',0))
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize)
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page)
#         return render_template("xijupian.html",mvs=_mvs,title=_title,pagination=pagination)
#
#     elif category == "zhanzhengpian":
#         _title = u"战争片"
#         pagesize = 24
#         page = int(request.args.get('page',0))
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize)
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page)
#         return render_template("zhanzhengpian.html",mvs=_mvs,title=_title,pagination=pagination)
#
#     elif category == "kehuanpian":
#         _title = u"科幻片"
#         pagesize = 24
#         page = int(request.args.get('page',0))
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize)
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page)
#         return render_template("kehuanpian.html",mvs=_mvs,title=_title,pagination=pagination)
#
#     elif category == "aiqingpian":
#         _title = u"爱情片"
#         pagesize = 24
#         page = int(request.args.get('page',0))
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize)
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page)
#         return render_template("aiqingpian.html",mvs=_mvs,title=_title,pagination=pagination)
#
#     elif category == "kongbupian":
#         _title = u"恐怖片"
#         pagesize = 24
#         page = int(request.args.get('page',0))
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize)
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page)
#         return render_template("kongbupian.html",mvs=_mvs,title=_title,pagination=pagination)
#
#     elif category == "juqingpian":
#         _title = u"剧情片"
#         pagesize = 24
#         page = int(request.args.get('page',0))
#         _mvs ,_count=  dw.get_movielist_by_cateen_page(category,page, pagesize)
#         pagination = Pagination(total=_count,prev_label=u"上一页",next_label=u"下一页",inner_window=8,per_page=pagesize, page=page)
#         return render_template("juqingpian.html",mvs=_mvs,title=_title,pagination=pagination)
#
#     else:
#         _title = u"TV山"
#         _dzmvs = dw.get_movielist_by_cateen_limit('dongzuopian',12)
#         _xjmvs = dw.get_movielist_by_cateen_limit('xijupian',12)
#         _warmvs = dw.get_movielist_by_cateen_limit('zhanzhengpian',12)
#         _khmvs = dw.get_movielist_by_cateen_limit('kehuanpian',12)
#         _aqmvs = dw.get_movielist_by_cateen_limit('aiqingpian',12)
#         _kbmvs = dw.get_movielist_by_cateen_limit('kongbupian',12)
#         _jqmvs = dw.get_movielist_by_cateen_limit('juqingpian',12)
#         return render_template("index.html.bak",title=_title,dzmvs=_dzmvs,xjmvs=_xjmvs,warmvs=_warmvs,khmvs=_khmvs,aqmvs=_aqmvs,kbmav=_kbmvs,jqmvs=_jqmvs)

@app.route("/dongzuopian/<name>.html")
def dongzuopian(name):
    _mv = dw.get_movie_by_cateen_name("dongzuopian",name)
    _title = _mv.title + " " +  u"动作片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title=_title,ls=_list)

@app.route("/xijupian/<name>.html")
def xijupian(name):
    _mv = dw.get_movie_by_cateen_name("xijupian",name)
    _title = _mv.title + " " +  u"喜剧片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title = _title,ls=_list)


@app.route("/zhanzhengpian/<name>.html")
def zhanzhengpian(name):
    _mv = dw.get_movie_by_cateen_name("zhanzhengpian",name)
    _title = _mv.title + " " +  u"战争片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title = _title,ls=_list)


@app.route("/kehuanpian/<name>.html")
def kehuanpian(name):
    _mv = dw.get_movie_by_cateen_name("kehuanpian",name)
    _title = _mv.title + " " +  u"科幻片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title = _title,ls=_list)


@app.route("/aiqingpian/<name>.html")
def aiqingpian(name):
    _mv = dw.get_movie_by_cateen_name("aiqingpian",name)
    _title = _mv.title + " " +  u"爱情片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title = _title,ls=_list)

@app.route("/kongbupian/<name>.html")
def kongbupian(name):
    _mv = dw.get_movie_by_cateen_name("kongbupian",name)
    _title = _mv.title + " " +  u"恐怖片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title = _title,ls=_list)

@app.route("/juqingpian/<name>.html")
def juqingpian(name):
    _mv = dw.get_movie_by_cateen_name("juqingpian",name)
    _title = _mv.title + " " +  u"剧情片"
    _list = dw.get_list_by_id(_mv.id)
    return render_template("detail.html.bak",mv=_mv,title = _title,ls=_list)

# @app.route("/player/<id>.html")
# def player(id):
#     _url = dw.get_player_by_id(id)
#     #print _url.res
#     #return _url.res
#     return render_template("player.html.bak",res = _url.res)
#首页
#@app.route("/")
#@app.route("/<category>")
#def index(category=''):
#    if category == "":
#        return render_template("index.html.bak")
#    elif category == "dongzuopian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("dongzuopian.html",mvs= _mvs)
#    elif category == "xijupian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("xijupian.html",mvs= _mvs)
#    elif category == "zhanzhengpian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("zhanzhengpian.html",mvs= _mvs)
#    elif category == "kehuanpian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("kehuanpian.html",mvs = _mvs)
#    elif category == "aiqingpian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("aiqingpian.html",mvs = _mvs)
#    elif category == "kongbupian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("kongbupian.html",mvs = _mvs)
#    elif category == "juqingpian":
#        _mvs = dw.get_movielist_by_catename_limit(category,12)
#        return render_template("juqingpian.html",mvs = _mvs)


##首页之前的备份
#@app.route('/')
#@app.route('/<category>')
#def index(category=''):
#    if category == '':
#        return render_template("index.html.bak")
#    elif category == 'dongzuo':
#        _mvs = dw.getQvodziByCategory(category,12)
#        return render_template('dongzuopian.html',mvs = _mvs)
#    elif category == 'xiju':
#        _mvs = dw.getQvodziByCategory(category,12)
#        return render_template('xijupian.html',mvs = _mvs)
#    elif category == 'aiqing':
#        _mvs = dw.getQvodziByCategory(category,12)
#        return render_template('aiqingpian.html',mvs = _mvs)
#    elif category == 'kehuan':
#        _mvs = dw.getQvodziByCategory(category,12)
#        return render_template('kehuanpian.html',mvs = _mvs)
#    elif category == 'kongbu':
#        _mvs = dw.getQvodziByCategory(category,12)
#        return render_template('kongbupian.html',mvs = _mvs)
#    else:
#        return render_template("index.html.bak")
#    # return redirect(url_for('admin.index'))


##分类
#@app.route('/category/')
#def category():
#    return render_template("category.html")
#
#
#@app.route('/guestbook/')
#def guestbook():
#    guestbooks = dw.getGuessbookLimit(10)
#    return render_template('guestbook.html',guestbooks = guestbooks)
#
#
#@app.route('/addguestbook',methods = ['GET','POST'])
#def addguestgook():
#    if request.method == 'POST':
#        _username = request.form['username']
#        _email = request.form['email']
#        _content = request.form['content']
#        _created = time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime(time.time())
#        guestbook = Guestbook()
#        guestbook.username = _username
#        guestbook.email = _email
#        guestbook.content = _content
#        #guestbook.created = _created
#        dw.insertGuestbook(guestbook)
#        return redirect('guestbook')
#    else:
#        return render_template('guestbook.html');


