#coding=utf8

from flask import Blueprint, render_template
from blog.data_wrapper import DataWrapper
dw = DataWrapper()

blog = Blueprint('blog',__name__,template_folder='templates')




@blog.route('/')
@blog.route('/page/<int:pid>')
def index(pid = 1):
    # cats = dw.get_all_category()
    # print len(cats)

    per_page = 2
    p = dw.get_category_by_page(pid,per_page)
    cats = p.items
    if not p.total:
        pagination = [0]
    elif p.total % per_page:
        pagination = range(1,p.total/per_page + 2)
    else:
        pagination = range(1,p.total/per_page + 1)



    return render_template('blog/index.html',cats=cats,
        pid=pid,
        pagination=pagination[:10],
        last_page = pagination[-1],
        nav_current="index")