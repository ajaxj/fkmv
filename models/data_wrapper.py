#coding=utf8
from model import Category

class DataWrapper(object):
    #查找全部的分类
    def get_all_category(self):
        return Category.query.all()

    #按分页查找分类
    def get_category_by_page(self,pageid,per_page):
        p_items = Category.query.paginate(pageid,per_page)
        return p_items




