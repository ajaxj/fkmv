#! /usr/bin/env python
#coding=utf-8

from flask import Module
account = Module(__name__)

@account.route("/login/",methods=("GET","POST"))
def login():
    pass
