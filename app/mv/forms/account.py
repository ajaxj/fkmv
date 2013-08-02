#!/usr/bin/env python
#coding=utf-8
from flask.ext.wtf import Form,TextField,TextAreaField,PasswordField,\
    SubmitField,Required,ValidationError

USERNAME = "admin"
PASSWORD = "1234"

class MyForm(Form):
    name = TextField("name",validators=[Required()])
    text = TextAreaField("txt")
    submit = SubmitField("Share")

class LoginForm(Form):
    username = TextField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Login")

    def validate_username(self,field):
        if field.data != USERNAME:
            raise ValidationError,"Invalid username"

    def validate_password(self,field):
        if field.data != PASSWORD:
            raise ValidationError,"Invalid password"
