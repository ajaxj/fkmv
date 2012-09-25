from fkmv.extensions import db

__author__ = 'Administrator'



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(100))
