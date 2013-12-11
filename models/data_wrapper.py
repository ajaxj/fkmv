# -*- coding:utf-8 -*-
from model import Movie,MovieList

class DataWrapper(object):

    def get_movielist_by_cateen_limit(self,cateen,limit):
        """取出电影通过分类和限定数量"""
        return Movie.query.filter_by(cateen=cateen).order_by(Movie.id.desc()).limit(limit).all()

    def get_movielist_by_cateen_page(self,cateen,page,pagesize):
        if page != 0:
            page = page -1
        offset = page * pagesize
        _mvs =  Movie.query.filter_by(cateen=cateen).order_by(Movie.id.desc()).offset(offset).limit(pagesize).all()
        _count = len( Movie.query.filter_by(cateen=cateen).all())
        return _mvs,_count

    def get_movie_by_cateen_name(self,cateen,name):
        return Movie.query.filter_by(cateen=cateen,name=name).first()

    def get_list_by_id(self,id):
        return MovieList.query.filter_by(mvid = id).all()

    def get_player_by_id(self,id):
        return MovieList.query.get(int(id))
