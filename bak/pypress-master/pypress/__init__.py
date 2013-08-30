#!/usr/bin/env python
#coding=utf-8
import os
import logging
import datetime
from logging.handlers import SMTPHandler,RotatingFileHandler
# TODO A
from flask import Flask
from pypress import views

from pypress.extensions import db,mail,cache,photos


DEFAULT_APP_NAME ='pypress'

DEFAULT_MODULES = (
    (views.frontend,""),
    (views.post,"/post"),
    (views.comment,"/comment"),
    (views.account,"/account"),
    (views.link,"/link"),
    (views.feeds,"/feeds"),
)


def create_app(config=None,modules=None):
    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)

    app.config.from_pyfile(config)
    configure_extensions(app)

    #提交前的拦截，用于登录
    configure_before_handlers(app)
    #TODO A

    configure_modules(app,modules)
    return app


def configure_extensions(app):
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    #TODO setup_themes(app)

#TODO A



def configure_before_handlers(app):
    @app.before_request
    def authenticate():
        #TODO 有补
        print "authenticate"


# 注册不同的模块
def configure_modules(app,modules):
    for module,url_prefix in modules:
        app.register_module(module,url_prefix=url_prefix)


def configure_logging(app):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')

    debug_log = os.path.join(app.root_path,
                             app.config['DEBUG_LOG'])

    debug_file_handler = \
        RotatingFileHandler(debug_log,
                            maxBytes=100000,
                            backupCount=10)

    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)

    error_log = os.path.join(app.root_path,
                             app.config['ERROR_LOG'])

    error_file_handler = \
        RotatingFileHandler(error_log,
                            maxBytes=100000,
                            backupCount=10)

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
