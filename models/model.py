#coding=utf8

from flask.ext.sqlalchemy import SQLAlchemy
from myapp import app

class nullpool_SQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(nullpool_SQLAlchemy, self).apply_driver_hacks(app,info,options)
        from sqlalchemy.pool import NullPool
        options['poolclass'] = NullPool
        del options['pool_size']

db = nullpool_SQLAlchemy(app)

class Category(db.Model):
    __tablename__ = 'mv_movie_hakuzycat'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True)

    def __unicode__(self):
        return self.name


# qvodzi 模型
class QvodziMovie(db.Model):
    __tablename__ = 'mv_qvodzi'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(200))
    img = db.Column(db.String(200))
    category = db.Column(db.String(50))
    location  = db.Column(db.String(50))
    banben = db.Column(db.String(50))
    pubdate = db.Column(db.String(50))
    lang = db.Column(db.String(50))
    arts = db.Column(db.String(50))
    year = db.Column(db.String(50))
    content = db.Column(db.Text)
    lists = db.Column(db.Text)
    tp = db.Column(db.String(50))
    dc = db.Column(db.String(100))
    status = db.Column(db.String(50))
    oldcontent = db.Column(db.Text)

    def __unicode__(self):
        return self.title







