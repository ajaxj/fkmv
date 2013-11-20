# -*-coding:utf-8 -*-
import urllib2
import MySQLdb
from BeautifulSoup import BeautifulSoup

#发布最后更新LIST表
class Sukupub:

    def parseList(self):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT list FROM suku_mv WHERE status = 1"
            cur = conn.cursor()
            cur.execute(sql)
            datalist = cur.fetchall()
            for data in datalist:

        except Exception,e:
            print e
        finally:
            cur.close()
            conn.close()



