#! /usr/bin/env python
#coding=utf-8
"""
    frontend.py
    ~~~~~~~~~~~~~
    :license: BSD, see LICENSE for more details.
"""

import datetime
import os

from flask import Module, Response, request, flash, jsonify, g, current_app,\
    abort, redirect, url_for, session, send_file, send_from_directory





frontend = Module(__name__)

@frontend.route("/")
def index():
    return "hello"


@frontend.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


