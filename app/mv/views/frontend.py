# -*- coding:utf-8 -*-


from flask import Module,Response,Request,flash,json,current_app, render_template
from app.mv.models.models import Category


frontend = Module(__name__)

@frontend.route("/")
def index():
    #日志的权别
    current_app.logger.debug("this is debug")
    current_app.logger.info("this is info")
    current_app.logger.warning("这是错误")
    current_app.logger.error("this is error")


    return render_template('layout.html')