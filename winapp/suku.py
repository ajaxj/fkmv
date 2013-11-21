
# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
import time
from BeautifulSoup import BeautifulSoup
import re



class Suku:
    #pwd = "273511"
    pwd = ""
    url_dongzuo = "http://www.suku.cc/film17/index.html"

    #读取远程地址内容
    def readUrlToHtml(self,url):
        try:
            req = urllib2.Request(url)
            res = urllib2.urlopen(req,timeout=30)
            _html = res.read()
            return _html
        except Exception,e:
            print e
            return None

    #解析HTML
    def parseListHtml(self,url):
        _html = self.readUrlToHtml(url)
        if _html is not None:
            #格式化utf-8
            if re.search(r'gb2312',_html,re.I):
                html = re.sub('gb2312','utf-8',_html)
                html = html.decode('gbk')
            soup = BeautifulSoup(html.encode('utf-8'))
            ul = soup.find('ul',{'class':'img-list'})
            li_list = ul.findAll('li')
            for li in li_list:
                _url = li.find('a').get('href')
                _title = li.find('img').get('alt')
                #TODO 这里要变不同的分类
                _cateen = "dongzuopian"
                _catecn = u"动作片"
                #_cateen = "xijupian"
                #_catecn = u"喜剧片"
                #
                result = self.insertListToDb(_title,_url,_cateen,_catecn)
                if result is False:
                    return False
            return True
        else:
            return False

    #插入列表页的MYSQL
    def insertListToDb(self,title,url,cateen,catecn):
        conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
        sql = "SELECT * FROM suku_mv WHERE title = '%s'" %(title)
        cur = conn.cursor()
        cur.execute(sql)
        if cur.fetchone() == None:
            sql = "INSERT INTO suku_mv(title,url,cateen,catecn)" \
                " VALUES ('%s','%s','%s','%s')" %(title,url,cateen,catecn)
            try:
                cur.execute(sql)
                conn.commit()
            except Exception,e:
                print e
                return False
            finally:
                cur.close()
                conn.close()
        return True

    #给抓取表添加分类和页号
    def addPagesByCategory(self,category,pagenum):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            cur = conn.cursor()
            for num in range(pagenum,0,-1):
                sql = "INSERT INTO suku_page (pagenum,category) VALUES('%d','%s')" %(num,category)
                cur.execute(sql)
                conn.commit()
            print category + " ok"
            return True
        except Exception,e:
            print e
            return False
        finally:
            cur.close()
            conn.close()

    # 2013 11 20 更新
    def initPages(self):
        #动作片 215
        self.addPagesByCategory("dongzuopian",215)
        #喜剧片 201
        self.addPagesByCategory("xijupian",201)
        #爱情片 96
        self.addPagesByCategory("aiqingpian",96)
        #科幻片 53
        self.addPagesByCategory("kehuanpian",53)
        #恐怖片 123
        self.addPagesByCategory("kongbupian",123)
        #战争片
        self.addPagesByCategory("zhanzhengpian",32)
        #剧情片
        self.addPagesByCategory("juqingpian",366)



    #主程序 category 代表分类
    def main_run(self,category):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM suku_page WHERE status = 0 and category='%s'" %(category)
            cur = conn.cursor()
            cur.execute(sql)

            #本地抓取的
            datalist = cur.fetchall()
            for data in datalist:
                #TODO 这里有不同的抓取页面要改
                url = "http://www.suku.cc/film17/index" + str(data[1]) +".html"
                #url = "http://www.suku.cc/film18/index" + str(data[1]) +".html"
                result = self.parseListHtml(url)
                if result:
                    sql = "update suku_page set status=1 where id=%d" %(int(data[0]))
                    cur.execute(sql)
                    conn.commit()
                    print url
                    time.sleep(2)
                else:
                    return False
            return True


            #这是放在服务器上处理的
            #data = cur.fetchone()
            #if data == None:
            #    return False
            #url = "http://www.suku.cc/film17/index" + str(data[1]) +".html"
            #result = self.parseListHtml(url)
            #if result:
            #    sql = "update suku_page set status=1 where id=%d" %(int(data[0]))
            #    cur.execute(sql)
            #    conn.commit()
            #    return True
        except Exception,e:
            print e
            return False
        finally:
            cur.close()
            conn.close()






if __name__ == '__main__':
    app = Suku()
    app.initPages()        #初始化页号
    #app.main_run("dongzuopian")
    #app.main_run("xijupian")
