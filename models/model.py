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


# hakuzy的列表,放着远程要抓取的地址和分类
class Hakuzy(db.Model):
    __tablename__ = "hakuzy"
    id = db.Column(db.Integer,primary_key=True)
    catename = db.Column(db.String(45))
    url = db.Column(db.String(200))
    status = db.Column(db.Integer)
    title = db.Column(db.String(100))
    location = db.Column(db.String(45))
    banben  = db.Column(db.String(50)) # 影片版本
    img = db.Column(db.String(200))  #图片地址
    arts = db.Column(db.String(200)) # 演员
    dc = db.Column(db.String(100))
    lang = db.Column(db.String(50))
    year = db.Column(db.String(50)) #上映日期
    state = db.Column(db.String(45))    #影片状态
    catecn = db.Column(db.String(45))
    content = db.Column(db.Text)
    lists = db.Column(db.Text)

    def __unicode__(self):
        return self.title


#hakuzy model
class HakuzyMovie(db.Model):
    __tablename__ = 'mv_movie_hakuzy'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    title1 = db.Column(db.String(45))
    title2 = db.Column(db.String(45))
    category = db.Column(db.String(200))
    location = db.Column(db.String(45))
    pubdate = db.Column(db.TIMESTAMP)
    url = db.Column(db.String(200))
    banben  = db.Column(db.String(50)) # 影片版本
    img = db.Column(db.String(200))  #图片地址
    arts = db.Column(db.String(100)) # 演员
    dc = db.Column(db.String(100))
    lang = db.Column(db.String(50))
    status = db.Column(db.String(50)) #影片状态
    year = db.Column(db.String(50)) #上映日期
    content = db.Column(db.Text)
    lists = db.Column(db.Text)
    ck = db.Column(db.Integer)

    def __unicode__(self):
        return self.title


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


#留言表
class Guestbook(db.Model):
    __tablename__ = 'guestbook'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))
    content = db.Column(db.Text)
    reply = db.Column(db.Text)
    created = db.Column(db.TIMESTAMP)

    def __unicode__(self):
        return self.message






