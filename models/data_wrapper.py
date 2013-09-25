#coding=utf8
from model import Category,QvodziMovie,HakuzyMovie,db

class DataWrapper(object):
    #查找全部的分类
    def get_all_category(self):
        return Category.query.all()

    #按分页查找分类
    def get_category_by_page(self,pageid,per_page):
        p_items = Category.query.paginate(pageid,per_page)
        return p_items

    #取出前十
    def get_hakuzymvlimit10(self):
        return HakuzyMovie.query.filter_by(ck = 0).limit(10).all()

    #通过ID取出hakuzy
    def get_hakuzymv_by_id(self,id):
        return HakuzyMovie.query.get(int(id))

    def update_hakuzymv(self,mv):
        db.session.add(mv)
        db.session.commit()


    # 取出前十
    def get_qvodzimvlimit10(self,category):
        return QvodziMovie.query.filter_by(category=category).limit(10).all()


    # 取出分类,并限定数量
    def getQvodziByCategory(self,category,limit):
        return QvodziMovie.query.filter_by(category=category).limit(limit).all()



