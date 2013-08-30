# -*- coding:utf-8 -*-
import sqlite3
from flask import Flask,request, render_template,redirect,url_for,abort,session,flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form,TextField,TextAreaField,PasswordField,SubmitField,Required,ValidationError
#配置
DEBUG = True
SQLALCHEMY_DATABASE_URL="sqlite:///flaskr.db"
SQLALCHEMY_ECHO = DEBUG
SECRET_KEY = "development key"
USERNAME = "admin"
PASSWORD = "default"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS',silent=True)



db = SQLAlchemy(app)

class Entry(db.Model):
    __tablename__ = "entries"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Unicode(200))
    text = db.Column(db.UnicodeText)

# db.create_all()

class EntryForm(Form):
    title = TextField("Title",validators=[Required()])
    text = TextAreaField("Test")
    submit = SubmitField("Share")

class LoginForm(Form):
    username = TextField("Username")
    password = PasswordField("Password")
    submit = SubmitField(u"登录")

    def validate_username(self,field):
        if field.data != USERNAME:
            raise ValidationError,"Invalid username"

    def validate_password(self,field):
        if field.data != PASSWORD:
            raise ValidationError,"Invalid password"



@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc())
    form = EntryForm()
    return render_template("show_entries.html",entries=entries,form = form)


@app.route('/add',methods=['POST'])
def add_entity():
    if not session.get('logined_in'):
        abort(401)

    form = EntryForm()
    if form.validate():
        entry = Entry()
        form.populate_obj(entry)
        db.session.add(entry)
        db.session.commit()
        flash('New entry was successfully posted')
    else:
        flash('You form errors')

    return redirect(url_for('show_entries'))


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('show_entries'))
    return render_template("login.html",form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('show_entries'));




if __name__ == '__main__':
    app.run()