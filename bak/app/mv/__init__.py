# coding:utf-8
import os
import logging
from logging.handlers import  RotatingFileHandler
from bak.app.mv.extensions import db
from bak.app.mv import views


__author__ = 'Administrator'


from flask import Flask

DEFAULT_APP_NAME = "mv"

DEFAULT_MODULES = (
    (views.frontend,""),
    (views.admin,"/admin")
)

def create_app(config=None,modules=None):
    if modules is None:
        modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)
    app.config.from_pyfile(config)
    configure_extensions(app)
    configure_logging(app)
    configure_modules(app,modules)
    return app


def configure_extensions(app):
    db.init_app(app)


#模块配置
def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)



#日志配置
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
