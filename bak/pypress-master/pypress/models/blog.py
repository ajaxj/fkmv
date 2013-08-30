#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from flask.ext.sqlalchemy import BaseQuery
from pypress.extensions import db

class PostQuery(BaseQuery):
    pass


class Post(db.Model):
    __tablename__ = 'posts'
    PER_PAGE = 40
    query_class = PostQuery

    id = db.Column(db.Integer,primary_key=True)
    author_id = db.Column(db.Integer) #TODO A
    _title = db.Column("title", db.Unicode(100), index=True)
    _slug = db.Column("slug", db.Unicode(50), unique=True, index=True)
    content = db.Column(db.UnicodeText)
    num_comments = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return "<%s>" % self


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer,primary_key = True)
    slug = db.Column(db.Unicode(80),unique=True)
    #TODO

class Comment(db.Model):
    __tablename__ = "comments"
    PER_PAGE = 40
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50))
    nickname = db.Column(db.Unicode(50))
    website = db.Column(db.String(100))
    #TODO A

class Link(db.Model):
    __tablename__ = 'links'
    PER_PAGE = 80
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Unicode(50),nullable=False)
    link = db.Column(db.String(100),nullable=False)
    logo = db.Column(db.String(100))
    description = db.Column(db.Unicode(100))
    email = db.Column(db.String(50))
    passed = db.Column(db.Boolean,default=False)
    create_date = db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)

    #TODO A
    def __str__(self):
        return self.name