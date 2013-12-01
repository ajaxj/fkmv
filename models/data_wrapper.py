# -*- coding:utf-8 -*-
from model import Movie,MovieList

class DataWrapper(object):

    def get_movielist_by_cateen_limit(self,cateen,limit):
        """取出电影通过分类和限定数量"""
        return Movie.query.filter_by(cateen=cateen).order_by(Movie.id.desc()).limit(limit).all()

    def get_movie_by_cateen_name(self,cateen,name):
        return Movie.query.filter_by(cateen=cateen,name=name).first()

    def get_list_by_id(self,id):
        return MovieList.query.filter_by(mvid = id).all()
