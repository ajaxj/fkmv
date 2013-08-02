# -*- coding:utf-8 -*-
import sqlite3
from flask import Flask,request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form,TextField,TextAreaField,PasswordField,SubmitField,Required
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

db.create_all()

class EntryForm(Form):
    title = TextField("Title",validators=[Required()])
    text = TextAreaField("Test")
    submit = SubmitField("Share")

class LoginForm(Form):
    username = TextField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Login")
    # TODO vilidate

@app.route('/')
def show_entries():
    entries = None
    form = EntryForm()
    return render_template("show_entries.html",entries=entries,form = form)
