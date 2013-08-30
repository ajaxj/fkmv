#coding=utf8
from data import Category


class DataWrapper(object):
    def get_all_category(self):
        return Category.query.all()

    def get_category_by_page(self,pid,per_page):
        p = Category.query.order_by(Category.id.desc()).paginate(pid,per_page)
        return p