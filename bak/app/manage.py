# coding=utf-8

from bak.app.mv import create_app

__author__ = 'Administrator'

from flask.ext.script import Manager

manager = Manager(create_app('config.cfg'))

if __name__ == "__main__":
    manager.run()