# coding:utf-8
from app.mv.extensions import db

__author__ = 'Administrator'


class HakuzyMovie(db.Model):
    __tablename__ = "mv_movie_hakuzy"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(200))

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return '<Movie %r>' % self.title




