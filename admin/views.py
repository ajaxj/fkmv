#coding=utf8

from flask import Blueprint, render_template, request, redirect, session, url_for
from models.data_wrapper import DataWrapper
dw = DataWrapper()

admin = Blueprint('admin',__name__,template_folder='templates')




@admin.route('/')
def index():
    if 'logined' in session:
        return render_template('admin/index.html')
    else:
        return render_template('admin/login.html')

@admin.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        _passwd =request.form['passwd']
        if _email =='ajaxj@qq.com' and _passwd == '1234':
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


