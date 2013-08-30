#coding=utf8
from flask import render_template

from myapp import app
from blog.views import blog
from admin.views import admin

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
        return render_template('dongzuo.html')
    elif category == 'xiju':
        return render_template('xiju.html')
    elif category == 'aiqing':
        return render_template('aiqing.html')
    elif category == 'kehuan':
        return render_template('kehuan.html')
    elif category == 'kongbu':
        return render_template('kongbu.html')
    else:
        return render_template("index.html")
    # return redirect(url_for('admin.index'))


#分类
@app.route('/category/')
def category():
    return render_template("category.html")


