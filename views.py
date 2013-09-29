#coding=utf8
from flask import render_template,request, redirect
import time
from models.model import Guestbook

from myapp import app
from blog.views import blog
from admin.views import admin

from models.data_wrapper import DataWrapper
dw = DataWrapper()

app.register_blueprint(blog,url_prefix="/blog")
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



#首页
@app.route('/')
@app.route('/<category>')
def index(category=''):
    if category == '':
        return render_template("index.html")
    elif category == 'dongzuo':
        _mvs = dw.getQvodziByCategory(category,12)
        return render_template('dongzuo.html',mvs = _mvs)
    elif category == 'xiju':
        _mvs = dw.getQvodziByCategory(category,12)
        return render_template('xiju.html',mvs = _mvs)
    elif category == 'aiqing':
        _mvs = dw.getQvodziByCategory(category,12)
        return render_template('aiqing.html',mvs = _mvs)
    elif category == 'kehuan':
        _mvs = dw.getQvodziByCategory(category,12)
        return render_template('kehuan.html',mvs = _mvs)
    elif category == 'kongbu':
        _mvs = dw.getQvodziByCategory(category,12)
        return render_template('kongbu.html',mvs = _mvs)
    else:
        return render_template("index.html")
    # return redirect(url_for('admin.index'))


#分类
@app.route('/category/')
def category():
    return render_template("category.html")


@app.route('/guestbook/')
def guestbook():
    guestbooks = dw.getGuessbookLimit(10)
    return render_template('guestbook.html',guestbooks = guestbooks)


@app.route('/addguestbook',methods = ['GET','POST'])
def addguestgook():
    if request.method == 'POST':
        _username = request.form['username']
        _email = request.form['email']
        _content = request.form['content']
        _created = time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime(time.time())
        guestbook = Guestbook()
        guestbook.username = _username
        guestbook.email = _email
        guestbook.content = _content
        #guestbook.created = _created
        dw.insertGuestbook(guestbook)
        return redirect('guestbook')
    else:
        return render_template('guestbook.html');


