# -*- coding:utf-8 -*-
from model import Movie,MovieList,Hahuzy_mv,Guobianyu_mv,db

class DataWrapper(object):

    #取出hakuzy 一种类型下的一定数量的mv
    def get_hakuzy_urllist_by_catename(self,cateen,limit):
        return Hahuzy_mv.query.filter_by(cateen=cateen).order_by(Hahuzy_mv.id.desc()).limit(limit).all()

    #通过ID取出hakuzy
    def get_hakuzy_by_id(self,id):
        return Hahuzy_mv.query.get(int(id))

    #更新修改的hakuzy
    def update_hakuzy(self,hakuzy):
        db.session.add(hakuzy)
        print db.session.commit()

    #取出guobianyu一种类型下的一定数量的mv
    def get_guobianyu_urllist_by_catename(self,cateen,limit):
        return Guobianyu_mv.query.filter_by(cateen=cateen).order_by(Guobianyu_mv.id.desc()).limit(limit).all()

    #通过ID取出guobianyu
    def get_guobianyu_by_id(self,id):
        return Guobianyu_mv.query.get(int(id))


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
