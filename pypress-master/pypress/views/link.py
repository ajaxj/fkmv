#!/usr/bin/env python
#coding:utf-8

from flask import Module

link = Module(__name__)

@link.route("/")
@link.route("/page/<int:page>/")
def index(page = 1):
    pass