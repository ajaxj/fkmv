#!/usr/bin/env python
#coding=utf-8

import uuid

from flask import Flask, current_app
#from flask.ext.script import Server, Shell, Manager, Command, prompt_bool
from flask.ext.script import Manager,Server,Shell,prompt_bool

from fkmv import create_app
from fkmv.extensions import db
from fkmv.models.users import User
manager = Manager(create_app('config.cfg'))

manager.add_command("runserver", Server('0.0.0.0',port=5000))

def _make_context():
    return dict(db=db)
manager.add_command("shell", Shell(make_context=_make_context))

@manager.command
def createall():
    "建立同步的数据库表"
    db.create_all()

@manager.command
def dropall():
    "清理数据库表"
    if prompt_bool("Are you sure ? You will lose all your data !"):
        db.drop_all()




#@manager.option('-r', '--role', dest='role', default="member")
#@manager.option('-n', '--number', dest='number', default=1, type=int)
#def createcode(role, number):
#    codes = []
#    usercodes = []
#    for i in range(number):
#        code = unicode(uuid.uuid4()).split('-')[0]
#        codes.append(code)
#        usercode = UserCode()
#        usercode.code = code
#        if role == "admin":
#            usercode.role = User.ADMIN
#        elif role == "moderator":
#            usercode.role = User.MODERATOR
#        else:
#            usercode.role = User.MEMBER
#        usercodes.append(usercode)
#    if number==1:
#        db.session.add(usercode)
#    else:
#        db.session.add_all(usercodes)
#    db.session.commit()
#    print "Sign up code:"
#    for i in codes:
#        print i
#    return


if __name__ == "__main__":
    manager.run()
