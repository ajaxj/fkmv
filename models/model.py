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



