# -*- coding:utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from myapp import app

class nullpool_SQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(nullpool_SQLAlchemy, self).apply_driver_hacks(app,info,options)
        from sqlalchemy.pool import NullPool
        options['poolclass'] = NullPool
        del options['pool_size']

db = nullpool_SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'user_mv'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), unique = True)
    #role = db.Column(db.SmallInteger, default = ROLE_USER)
    #posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Movie(db.Model):
    __tablename__ = 'zhuzhu_mv'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    cateen = db.Column(db.String(45))
    catecn = db.Column(db.String(45))
    url = db.Column(db.String(200))
    title = db.Column(db.String(100))
    banben = db.Column(db.String(45))
    arts = db.Column(db.String(200))
    lang = db.Column(db.String(45))
    location = db.Column(db.String(45))
    pubdate = db.Column(db.String(45))
    content = db.Column(db.Text())
    list = db.Column(db.Text())
    status = db.Column(db.Integer)
    img = db.Column(db.String(255))
    pubyear = db.Column(db.String(100))

    def __unicode__(self):
        return self.title

class MovieList(db.Model):
    __tablename__ = 'zhuzhu_ls'
    id = db.Column(db.Integer,primary_key=True)
    mvid = db.Column(db.Integer)
    txt = db.Column(db.String(45))
    res = db.Column(db.Text())
    url = db.Column(db.String(100))

    def __unicode__(self):
        return self.txt


# class Hakuzy(db.Model):
    # __tablename__ = "hakuzy_mv"





