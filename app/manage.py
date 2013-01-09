# coding=utf-8

from mv import create_app

__author__ = 'Administrator'



from flask import Flask,g,session,request
from flask.ext.script import Server,Manager

manager = Manager(create_app('config.cfg'))

if __name__ == "__main__":
    manager.run()