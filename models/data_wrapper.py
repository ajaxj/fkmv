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

    def get_player_by_id(self,id):
        return MovieList.query.get(int(id))


    #后台hakuzy

    #通过分类,取得没有抓取的hakuzy的urllist 表,10个一组
    def get_hakuzy_urllist_by_catename(self,catename):
        return

