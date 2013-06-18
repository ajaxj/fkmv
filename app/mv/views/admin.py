# -*- coding:utf-8 -*-

from flask import Module,Response,Request,json, render_template
from app.mv.models.hakuzy import HakuzyMovie

admin = Module(__name__)

@admin.route("/")
def index():
    return render_template('admin/layout.html')


@admin.route('/hakuzymovies')
def hakuzymovies():
    movie = HakuzyMovie.query.first()
    movies = HakuzyMovie.query.limit(3).all()
    print movie.title
    print movies,movies[0].title
    return render_template('admin/hakuzymovies.html', movies= movies)
