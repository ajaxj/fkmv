#coding=utf8
import urllib2
from BeautifulSoup import BeautifulSoup
from flask import Blueprint, render_template, request, redirect, session, url_for
from forms.account import LoginForm
from models.data_wrapper import DataWrapper
from models.model import Movie
dw = DataWrapper()


# 使用Blueprint 的方式指明模块,并且定义模板的地址
admin = Blueprint('admin',__name__,template_folder='templates')

@admin.route('/')
def index():
    if 'logined' in session:
        return render_template('admin/index.html')
    else:
        return render_template('admin/login.html')

@admin.route('/movielist/<string:catename>')
def movielist(catename='dongzuopian'):
    movielist = dw.get_movielist_by_catename(catename)
    return render_template('admin/movielist.html',movielist=movielist)


@admin.route('/guestbook')
def guestbook():
    if 'logined' in session:
        return render_template('admin/guestbook.html')
    else:
        return render_template('admin/login.html')

#删除
@admin.route('/delgbook')
def delgbook():
    if 'logined' in session:
        return "pass"
    else:
        return render_template('admin/login.html')

#回复
@admin.route('/replygbook')
def replygbook():
    if 'logined' in session:
        return 'pass'
    else:
        return render_template('admin/login.html')



#hakuzy全列表


#通过分类名取得没有抓取的10条
@admin.route('/hakuzylist/<string:catename>')
def hakuzylist(catename='dongzuopian'):
    hakuzylist = dw.get_hakuzy_urllist_by_catename(catename)
    return render_template("admin/hakuzylist.html",hakuzylist=hakuzylist)

#抓取并更新数据库
@admin.route('/hakuzyurlfetch/')
def hakuzyurlfetch():
    _id = request.args.get('id','')
    hakuzy = dw.get_hakuzy_by_id(_id)
    url =  hakuzy.url
    try:
        res = urllib2.urlopen(url,timeout=50)
        s = res.read()
        soup = BeautifulSoup(s)
        table_list = soup.findAll('table')
        _img = table_list[4].find('img').get('src')
        td_list = table_list[5].findAll('td')
        _title = td_list[0].text.replace(u'影片名称：影片名称开始代码','').replace(u'影片名称结束代码','')
        _banben = td_list[1].text.replace(u'影片版本：影片副标开始代码','').replace(u'影片副标结束代码','')
        _arts = td_list[2].text.replace(u'影片演员：影片演员开始代码','').replace(u'影片演员结束代码','')
        _dc = td_list[3].text.replace(u'影片导演：影片导演开始代码','').replace(u'影片导演结束代码','')
        _category = td_list[4].text.replace(u'影片类型：影片类型开始代码','').replace(u'影片类型结束代码','')
        _lang = td_list[5].text.replace(u'影片语言：影片语言开始代码','').replace(u'影片语言结束代码','')
        _location = td_list[6].text.replace(u'影片地区：影片地区开始代码','').replace(u'影片地区结束代码','')
        _pubdate = td_list[7].text.replace(u'更新时间：影片更新时间开始代码','').replace(u'影片更新时间结束代码','')
        _status = td_list[8].text.replace(u'影片状态：','').replace(u'影片状态开始代码','').replace(u'影片状态结束代码','')
        _year = td_list[9].text.replace(u'上映日期：上映日期开始代码','').replace(u'上映日期结束代码','')
        _content = td_list[10].text.replace(u'影片介绍开始代码','').replace(u'影片介绍结束代码','')
        _lists =  table_list[6]
        hakuzy.title = _title
        hakuzy.banben = _banben
        hakuzy.arts = _arts
        hakuzy.dc = _dc
        hakuzy.catecn = _category
        hakuzy.lang = _lang
        hakuzy.location = _location
        hakuzy.state = _status
        hakuzy.year = _year
        hakuzy.content = _content
        hakuzy.lists = _lists
        hakuzy.status = 1   #抓取成功了
        hakuzy.img = _img
        dw.update_hakuzy(hakuzy)
    except Exception,e:
        print e
        return "err"
    return "ok"


#抓取成功的前20条通过分类名
@admin.route('/hakuzyfetchlist/<string:catename>')
def hakuzyfetchlist(catename='dongzuopian'):
    hakuzylist  = dw.get_hakuzy_by_catename(catename)
    return render_template("admin/hakuzyfetchlist.html",hakuzylist= hakuzylist)

@admin.route('/hakuzypush/')
def hakuzypush():
    _id = request.args.get('id','')
    hakuzy = dw.get_hakuzy_by_id(int(_id))
    mv = Movie()
    mv.title = hakuzy.title
    mv.banben = hakuzy.banben
    mv.arts = hakuzy.arts
    mv.catecn = hakuzy.catecn
    mv.catename = hakuzy.catename
    mv.content = hakuzy.content
    mv.dc = hakuzy.dc
    mv.lang = hakuzy.lang
    mv.year = hakuzy.year
    mv.img = hakuzy.img
    mv.lists = hakuzy.lists
    mv.location = hakuzy.location
    dw.insert_movie(mv)
    hakuzy.status = 3
    dw.update_hakuzy(hakuzy)
    return "ok"



#修正数据
@admin.route('/handlehakuzy/',methods=['GET','POST'])
def handlehakuzy():
    if request.method == 'POST':
        _id = request.form['id']
        hakuzy = dw.get_hakuzy_by_id(_id)
        _title =  request.form['title']
        _catecn = request.form['catecn']
        _banben = request.form['banben']
        _location = request.form['location']
        _arts = request.form['arts']
        _dc = request.form['dc']
        _lang = request.form['lang']
        _year = request.form['year']
        _state = request.form['state']
        _content = request.form['content']
        _status = request.form['status']
        _lists = request.form['lists']
        hakuzy.title = _title
        hakuzy.banben = _banben
        hakuzy.arts = _arts
        hakuzy.dc = _dc
        hakuzy.catecn = _catecn
        hakuzy.lang = _lang
        hakuzy.location = _location
        hakuzy.state = _state
        hakuzy.year = _year
        hakuzy.content = _content
        hakuzy.lists = _lists
        hakuzy.status = _status
        #hakuzy.img = _img
        dw.update_hakuzy(hakuzy)
        return redirect('admin/hakuzyfetchlist/dongzuopian')

    else:
        _id = request.args.get('id','')
        hakuzy = dw.get_hakuzy_by_id(_id)
        return render_template("admin/handlehakuzy.html",hakuzy = hakuzy)




@admin.route('/hakuzyall/')
def hakuzyall():
    if 'logined' in session:
        mvs = dw.get_hakuzymvlimit10()
        return render_template('admin/hakuzyall.html',mvs= mvs)
    else:
        return render_template('admin/login.html')


#抓取并更新
@admin.route('/fetchhakuzy/')
def fetchhakuzy():
    if 'logined' in session:
        _id = request.args.get('id', '')
        mv = dw.get_hakuzymv_by_id(_id)
        url = "http://www.hakuzy.com" + mv.url
        try:
            res = urllib2.urlopen(url,timeout=30)
            s = res.read()
            soup = BeautifulSoup(s)
            table_list = soup.findAll('table')
            _img = table_list[4].find('img').get('src')
            td_list = table_list[5].findAll('td')
            _title = td_list[0].text.replace(u'影片名称：影片名称开始代码','').replace(u'影片名称结束代码','')
            _banben = td_list[1].text.replace(u'影片版本：影片副标开始代码','').replace(u'影片副标结束代码','')
            _arts = td_list[2].text.replace(u'影片演员：影片演员开始代码','').replace(u'影片演员结束代码','')
            _dc = td_list[3].text.replace(u'影片导演：影片导演开始代码','').replace(u'影片导演结束代码','')
            _category = td_list[4].text.replace(u'影片类型：影片类型开始代码','').replace(u'影片类型结束代码','')
            _lang = td_list[5].text.replace(u'影片语言：影片语言开始代码','').replace(u'影片语言结束代码','')
            _location = td_list[6].text.replace(u'影片地区：影片地区开始代码','').replace(u'影片地区结束代码','')
            _pubdate = td_list[7].text.replace(u'更新时间：影片更新时间开始代码','').replace(u'影片更新时间结束代码','')
            _status = td_list[8].text.replace(u'影片状态：','').replace(u'影片状态开始代码','').replace(u'影片状态结束代码','')
            _year = td_list[9].text.replace(u'上映日期：上映日期开始代码','').replace(u'上映日期结束代码','')
            _content = td_list[10].text.replace(u'影片介绍开始代码','').replace(u'影片介绍结束代码','')
            _lists =  table_list[6]
            mv.title = _title
            mv.banben = _banben
            mv.arts = _arts
            mv.dc = _dc
            mv.category = _category
            mv.lang = _lang
            mv.location = _location
            mv.status = _status
            mv.year = _year
            mv.content = _content
            mv.lists = _lists
            mv.img = _img
            mv.ck = 1
            dw.update_hakuzymv(mv)

            return "fetch"
        except Exception,e:
            print e
    else:
        return render_template('admin/login.html')




@admin.route("/adminlogin", methods=("GET","POST"))
def adminlogin():
    form = LoginForm()
    return render_template('admin/adminlogin.html',form=form)


@admin.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        _passwd =request.form['passwd']
        if _email =='1' and _passwd == '1':
            session['logined'] = True
            return redirect("/admin/")
        else:
            return render_template('admin/login.html')
    else:
        return render_template('admin/login.html')

@admin.route('/logout')
def logout():
    session.pop('logined',None)
    return redirect(url_for('admin.login'))


@admin.route('/qvodzimv')
def qvodzimv():
    category = "dongzuo"
    mvs = dw.get_qvodzimvlimit10(category)
    # for mv in mvs:
    #     print mv.title
    return render_template('admin/qvodzimv.html',mvs = mvs)



# 所有分类和分页
@admin.route('/categories')
@admin.route('/categories/page/<int:pageid>')
def categories(pageid = 1):
    per_page = 10       #每页十个

    p = dw.get_category_by_page(pageid,per_page)
    _categories = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1,p.total/per_page + 2)
    else:
        pagination = range(1,p.total/per_page + 1)
    return render_template('admin/categories.html',
                           categories = _categories,
                           pageid = pageid,
                           pagination=pagination[:10],
                           last_page = pagination[-1],
                           nav_current="index")


def movies(pageid = 1):
    per_page = 10


