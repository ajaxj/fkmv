#!/usr/bin/env python
#coding=utf-8
import datetime
import os
from flask import Module

frontend = Module(__name__)

@frontend.route("/")
def index(year=None,month=None,day=None,page=1):
    if page<1:page=1

    return "index"




