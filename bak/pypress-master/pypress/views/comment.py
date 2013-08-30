#! /usr/bin/env python
#coding=utf-8

from flask import Module

comment = Module(__name__)

@comment.route("/<int:comment_id>/delete/",methods=("POST",))
def delete(comment_id):
    pass
