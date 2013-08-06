# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from flask.ext.wtf import Form,TextField,Required,SubmitField


class YetwoCategoryForm(Form):
    name = TextField("name",validators=[Required])
    submit= SubmitField('sub')


