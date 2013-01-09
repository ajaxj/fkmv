from mv.extensions import db

class User(db.Model):
    __tablename__ = "mv_users"
    id =  db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)

class Category(db.Model):
    __tablename__ = "mv_category"
    id = db.Column(db.Integer,primary_key=True)