# -*- coding:utf-8 -*-

from flask import Module,Response,Request,json

admin = Module(__name__)

@admin.route("/")
def index():
    return "admin index"

