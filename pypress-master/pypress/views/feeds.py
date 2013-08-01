#! /usr/bin/env python
#coding=utf-8

from flask import Module

feeds = Module(__name__)

@feeds.route('/')
def index():
    pass