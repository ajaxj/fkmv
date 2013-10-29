# -*- coding:utf-8 -*-

from flask.ext.wtf import Form,TextField,PasswordField

#管理登录
class LoginForm(Form):
    login  = TextField("admin name")
    password = PasswordField("password")

#注册管理
class SingupForm(Form):
    adminname = TextField()
    adminpass = TextField()