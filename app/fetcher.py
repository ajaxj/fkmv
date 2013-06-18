# coding: utf-8
import os
import urllib2
import MySQLdb
import sys

__author__ = 'Administrator'

# 手工抓取的代码
class Fetcher:
    host = "localhost"
    user = "root"
    pwd = ""
    db = "ajaxj"


    def fetcher_img(self,id):
        conn = MySQLdb.connect(host=self.host,user=self.user,passwd = self.pwd,db=self.db,charset="utf8")
        sql = "SELECT * FROM mv_movie_hakuzy WHERE id = '%d'" %(int(id))
        cur = conn.cursor()
        try:
            cur.execute(sql)
            mv = cur.fetchone()
            print mv[3]
        except Exception,e:
            print e
            sys.exit(1)
        finally:
            cur.close()
            conn.close()

    def downimg(self,):
        path = r'%s'%("d:/projects/github/ajaxj/fkmv/app/data/")
        # path = os.path.abspath('.') # 这样也可以取当前目录
        url = "http://img.cnjuc.com/pic/uploadimg/2009/9/29/20090929183448858.jpg"
        sock=urllib2.urlopen(url)
        file=sock.read()
        sock.close()
        f = open(path,'wb')
        try:
            f.write(file)
            f.flush()
        except Exception,e:
            print e
        finally:
            f.close()




if __name__ == "__main__":
    obj = Fetcher()
    # obj.fetcher_img(1)
    obj.downimg()
