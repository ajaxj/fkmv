#coding=utf8
from model import Category,QvodziMovie,HakuzyMovie,Guestbook,db,Hakuzy

class DataWrapper(object):



    #通过分类 取得hakuzy的 urllist 表,
    def get_hakuzy_urllist_by_catename(self,catename):
        return Hakuzy.query.filter_by(catename=catename).all()


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


# ****************  Guestbook *********************#
    #添加留言
    def insertGuestbook(self,guestbook):
        db.session.add(guestbook)
        db.session.commit()

    #取得LIMIT的数量的留言
    def getGuessbookLimit(self,limit):
        return Guestbook.query.limit(limit).all()

    #更新或者回复
    def updateGuestbook(self,guestbook):
        db.session.add(guestbook)
        db.session.commit()

    #删除留言通过ID
    def delelteGuestbook(self,id):
        guestbook = Guestbook.query.get(int(id))
        db.session.delete(guestbook)
        db.session.commit()
