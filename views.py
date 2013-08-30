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



@app.route('/')
def index():
    return render_template("index.html")
    # return redirect(url_for('admin.index'))
