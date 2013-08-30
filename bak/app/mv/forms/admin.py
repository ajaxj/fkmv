#!/usr/bin/env python
#coding=utf-8
from flask.ext.wtf import Form,TextField,PasswordField,SubmitField,required,ValidationError

ADMINUSER = 'admin'
ADMINPASS = '1234'


#管理员账号 Form类
class AdminForm(Form):
    adminuser = TextField(u"账号")
    adminpass  = PasswordField(u"密码")
    submit = SubmitField(u"登录")

    #验证账号
    def validate_username(self,field):
        if field.data != ADMINUSER:
            raise ValidationError,'Invalid Admin User'

    def validate_password(self,field):
        if field.data != ADMINPASS:
            raise ValidationError,"Invalid Admin Pass"


