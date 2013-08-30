# !/usr/bin/env python
# coding: utf-8
import uuid
from flask.ext.script import Server,Shell,Manager, prompt_bool
from pypress import create_app
from pypress.extensions import db
from pypress.models.users import User,UserCode

manager = Manager(create_app("config.cfg"))
manager.add_command("runserver",Server('0.0.0.0',port=8080))

def _make_context():
    return dict(db=db)
manager.add_command("shell",Shell(make_context=_make_context))

@manager.command
def createall():
    db.create_all()

@manager.command
def dropall():
    if prompt_bool("Are you sure? You will lose all your data!"):
        db.drop_all()


# python manage.py hello -n Joe -u reddit.com
#python manage.py hello --name=Joe --url=reddit.com
@manager.option('-n', '--name', dest='name', default='joe')
@manager.option('-u', '--url', dest='url', default=None)
def hello(name, url):
    if url is None:
        print "hello", name
    else:
        print "hello", name, "from", url

@manager.option('-r','--role',dest='role',default='member')
@manager.option('-n','--number',dest='number',default=1,type=int)
def createcode(role,number):
    codes = []
    usercodes = []
    for i in range(number):
        code = unicode(uuid.uuid4()).split('-')[0]
        codes.append(code)
        usercode = UserCode()
        usercode.code = code
        if role == 'admin':
            usercode.role = User.ADMIN
        elif role== 'moderator':
            usercode.role = User.MODERATOR
        else:
            usercode.role = User.MEMBER
        usercodes.append(usercode)
    if number == 1:
        db.session.add(usercode)
    else:
        db.session.add_all(usercodes)
    db.session.commit()
    print "Sign up code:"
    for i in codes:
        print i
    return


if __name__ == "__main__":
    manager.run()
