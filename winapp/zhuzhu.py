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
    def parseListHtml(self,url,category):
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
                img = li.find('img')
                if img != None:
                    _img =  img.get('src')
                else:
                    _img = ""
                span = li.find('span')
                if span != None:
                    _banben = span.string
                else:
                    _banben = ""
                if len(a_list) > 0:
                    _title = a_list[1].string
                    _url = a_list[1].get('href')
                    if category == 'dongzuopian':
                        _cateen = "dongzuopian"
                        _catecn = u"动作片"
                    elif category == 'xijupian':
                        _cateen = "xijupian"
                        _catecn = u"喜剧片"
                    elif category == 'aiqingpian':
                        _cateen = "aiqingpian"
                        _catecn = u"爱情片"
                    elif category == 'kehuanpian':
                        _cateen = "kehuanpian"
                        _catecn = u"科幻片"
                    elif category == 'kongbupian':
                        _cateen = "kongbupian"
                        _catecn = u"恐怖片"
                    elif category == 'zhanzhengpian':
                        _cateen = "zhanzhengpian"
                        _catecn = u"战争片"
                    elif category == 'juqingpian':
                        _cateen = "juqingpian"
                        _catecn = u"剧情片"

                    result = self.insertListToDb(_title,_url,_cateen,_catecn,_banben,_img)
                    if result is False:
                        return False
            return True
        else:
            return False



    # 插入列表页的MYSQL MV名,远程地址,分类英文,分类中文,版本，图片
    def insertListToDb(self,title,url,cateen,catecn,banben,img):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM zhuzhu_mv WHERE title = '%s'" %(title)
            cur = conn.cursor()
            cur.execute(sql)
            if cur.fetchone() == None:
                sql = "INSERT INTO zhuzhu_mv(title,url,cateen,catecn,banben,img) VALUES ('%s','%s','%s','%s','%s','%s')" %(title,url,cateen,catecn,banben,img)
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

    # 2013 11 22 更新
    def initPages(self):
        #动作片 125    http://www.zhuzhu.cc/dz/index125.html
        self.addPagesByCategory("dongzuopian",125)
        #喜剧片 152 http://www.zhuzhu.cc/xj/index152.html
        self.addPagesByCategory("xijupian",152)
        #爱情片 96  http://www.zhuzhu.cc/aq/index74.html
        self.addPagesByCategory("aiqingpian",74)
        #科幻片 53 http://www.zhuzhu.cc/kh/index48.html
        self.addPagesByCategory("kehuanpian",48)
        #恐怖片 123 http://www.zhuzhu.cc/kb/index115.html
        self.addPagesByCategory("kongbupian",115)
        #战争片    http://www.zhuzhu.cc/war/index18.html
        self.addPagesByCategory("zhanzhengpian",18)
        #剧情片    http://www.zhuzhu.cc/jq/index272.html
        self.addPagesByCategory("juqingpian",272)

    #主程序 category 代表分类
    def main_run(self,category):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM zhuzhu_page WHERE status = 0 and category='%s'" %(category)
            cur = conn.cursor()
            cur.execute(sql)

            #本地抓取的
            datalist = cur.fetchall()
            for data in datalist:
                #TODO 这里有不同的抓取页面要改
                if category == 'dongzuopian':
                    url = "http://www.zhuzhu.cc/dz/index" + str(data[1]) +".html"
                elif category == 'xijupian':
                    url = "http://www.zhuzhu.cc/xj/index" + str(data[1]) +".html"
                elif category == 'aiqingpian':
                    url = "http://www.zhuzhu.cc/aq/index" + str(data[1]) +".html"
                elif category == 'kehuanpian':
                    url = "http://www.zhuzhu.cc/kh/index" + str(data[1]) +".html"
                elif category == 'kongbupian':
                    url = "http://www.zhuzhu.cc/kb/index" + str(data[1]) +".html"
                elif category == 'zhanzhengpian':
                    url = "http://www.zhuzhu.cc/war/index" + str(data[1]) +".html"
                elif category == 'juqingpian':
                    url = "http://www.zhuzhu.cc/jq/index" + str(data[1]) +".html"

                result = self.parseListHtml(url,category)
                if result:
                    sql = "update zhuzhu_page set status=1 where id=%d" %(int(data[0]))
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

    #之前更新了大部分。现在更新前几页
    def main_run2(self,category,pagenum):
        for i in range(pagenum):
            if category == "dongzuopian":
                if i == 0:
                    url = "http://www.zhuzhu.cc/dz/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/dz/index" + str(i+1) +".html"
            elif category == 'xijupian':
                if i == 0:
                    url = "http://www.zhuzhu.cc/xj/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/xj/index" + str(i+1) +".html"
            elif category == 'aiqingpian':
                if i == 0:
                    url = "http://www.zhuzhu.cc/aq/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/aq/index" + str(i+1) +".html"
            elif category == 'kehuanpian':
                if i == 0:
                    url = "http://www.zhuzhu.cc/kh/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/kh/index" + str(i+1) +".html"
            elif category == 'kongbupian':
                if i == 0:
                    url = "http://www.zhuzhu.cc/kb/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/kb/index" + str(i+1) +".html"
            elif category == 'zhanzhengpian':
                if i == 0:
                    url = "http://www.zhuzhu.cc/war/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/war/index" + str(i+1) +".html"
            elif category == 'juqingpian':
                if i == 0:
                    url = "http://www.zhuzhu.cc/jq/index.html.bak"
                else:
                    url = "http://www.zhuzhu.cc/jq/index" + str(i+1) +".html"


            result = self.parseListHtml(url,category)
            print result

if __name__ == "__main__":
    app = Zhuzhu()

    app.main_run2("dongzuopian",10)
    app.main_run2("xijupian",10)
    app.main_run2("aiqingpian",10)
    app.main_run2("kehuanpian",10)
    app.main_run2("kongbupian",10)
    app.main_run2("zhanzhengpian",10)
    app.main_run2("juqingpian",10)

    #app.initPages()        #初始化页号
    #app.main_run("dongzuopian")
    #app.main_run("xijupian")
    #app.main_run("aiqingpian")
    #app.main_run("kehuanpian")
    #app.main_run("kongbupian")
    #app.main_run("zhanzhengpian")
    #app.main_run("juqingpian")




