#!/usr/bin/env python
#coding=utf-8
import datetime
import os
import json

from flask import Module

post = Module(__name__)

@post.route("/",methods=("GET","POST"))
def submit():
    pass
