# -*- coding:utf-8 -*-

from flask import Module,Response,Request,flash,json

frontend = Module(__name__)

@frontend.route("/")
def index():
    return "Home index"