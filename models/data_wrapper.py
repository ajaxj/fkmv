#coding=utf8
from model import Category,QvodziMovie,HakuzyMovie,Guestbook,db,Hakuzy,Movie

class DataWrapper(object):

    #取出正式的电影列表通过分类英文名称
    def get_movielist_by_catename(self,catename):
        return Movie.query.filter_by(catename = catename).all()

    #取出正式的电影列表,通过分类,并限定数量
    def get_movielist_by_catename_limit(self,catename,limit):
        return Movie.query.filter_by(catename=catename).order_by(Movie.id.desc()).limit(limit).all()


    #插入movie
    def insert_movie(self,movie):
        db.session.add(movie)
        db.session.commit()

    #通过分类 取得没有抓取hakuzy的 urllist 表,10个一组
    def get_hakuzy_urllist_by_catename(self,catename):
        return Hakuzy.query.filter_by(catename=catename,status = 0).limit(10).all()

    #通过分类 取得抓取hakuzy的已经抓取
    def get_hakuzy_by_catename(self,catename):
        return Hakuzy.query.filter(Hakuzy.catename == catename,Hakuzy.status > 0,Hakuzy.status < 3).limit(20).all()

    #通过ID取的hakuzy
    def get_hakuzy_by_id(self,id):
        return Hakuzy.query.get(int(id))

    def update_hakuzy(self,hakuzy):
        db.session.add(hakuzy)
        print db.session.commit()


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
