# -*- coding:utf-8 -*-
import logging
import logging.config
import urllib2
import MySQLdb
import time
from BeautifulSoup import BeautifulSoup
import re

#采集分类列表和更新MV内容
class Zhuzhu:
    pwd = ""
    logger = None


    def __init__(self):
        logging.config.fileConfig("logging.conf")
        self.logger = logging.getLogger("zhuzhu")



    #抓取远程URL转成HTML
    def readUrlToHtml(self,url):
        try:
            req = urllib2.Request(url)
            res = urllib2.urlopen(req,timeout=30)
            _html = res.read()
            return _html
        except Exception,e:
            self.logger.error(e.message)
            return None

    #抓取解析列表页面,并入库
    def paresListHtml(self,url):
        _html = self.readUrlToHtml(url)
        if _html is not None:
            if re.search(r'gb2312',_html,re.I):
                html = re.sub('gb2312','utf-8',_html)
                html = html.decode('gbk')
            soup = BeautifulSoup(html.encode('utf-8'))
            div = soup.find('div',{'class':'commend border1 mb6 channel'})
            li_list = div.findAll('li')
            for li in li_list:
                a_list = li.findAll('a')
                #TODO 不抓取图片和banben
                #img = li.find('img')
                #if img != None:
                #    _img =  img.get('src')
                span = li.find('span')
                #if span != None:
                #    _banben = span.string
                if len(a_list) > 0:
                    _title = a_list[1].string
                    _url = a_list[1].get('href')
                    _cateen = "dongzuopian"
                    _catecn = u"动作片"
                    result = self.insertListToDb(_title,_url,_cateen,_cateen)
                    if result is False:
                        return False
            return True
        else:
            return False



    # 插入列表页的MYSQL MV名,远程地址,分类英文,分类中文
    def insertListToDb(self,title,url,cateen,catecn):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM zhuzhu_mv WHERE title = '%s'" %(title)
            cur = conn.cursor()
            cur.execute(sql)
            if cur.fetchone() == None:
                sql = "INSERT INTO zhuzhu_mv(title,url,cateen,catecn) VALUES ('%s','%s','%s','%s')" %(title,url,cateen,catecn)
                cur.execute(sql)
                conn.commit()
                return True
        except Exception,e:
            self.logger.error(e.message)
            return False
        finally:
            cur.close()
            conn.close()


    #给抓取表添加分类和页号
    def addPagesByCategory(self,category,pagenum):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            cur = conn.cursor()
            for num in range(pagenum,0,-1):
                sql = "INSERT INTO zhuzhu_page (pagenum,category) VALUES('%d','%s')" %(num,category)
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




if __name__ == "__main__":
    app = Zhuzhu()
    url = "http://www.zhuzhu.cc/dz/"
    print app.paresListHtml(url)






