# coding:utf-8

from mv import views
from mv.extensions import db

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
    configure_modules(app,modules)
    return app


def configure_extensions(app):
    db.init_app(app)

def configure_modules(app, modules):
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)