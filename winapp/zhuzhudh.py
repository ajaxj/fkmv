# -*- coding:utf-8 -*-

#采集动漫
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import MySQLdb
import time


class Zhuzhudm:
    pwd = ""

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
    def parseListHtml(self,url):
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


                if _banben != None:
                    if re.search(u'集',_banben):
                        _ji = 1
                    else:
                        _ji = 0
                else:
                    _banben = ""
                    _ji = 0

                if len(a_list) > 0:
                    _title = a_list[1].string
                    _url = a_list[1].get('href')
                    _cateen = "donghuapian"
                    _catecn = u"动画片"
                    #print _title,_url,_cateen,_catecn,_banben,_img,_ji
                    result = self.insertListToDb(_title,_url,_cateen,_catecn,_banben,_img,_ji)
                    if result is False:
                        return False
            return True
        else:
            return False


    # 插入列表页的MYSQL MV名,远程地址,分类英文,分类中文,版本，图片
    def insertListToDb(self,title,url,cateen,catecn,banben,img,li):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM zhuzhudh_mv WHERE title = '%s'" %(title)
            cur = conn.cursor()
            cur.execute(sql)
            if cur.fetchone() == None:
                sql = "INSERT INTO zhuzhudh_mv(title,url,cateen,catecn,banben,img,ji) VALUES ('%s','%s','%s','%s','%s','%s',%d)" %(title,url,cateen,catecn,banben,img,li)
                cur.execute(sql)
                conn.commit()
                return True
        except Exception,e:
            print e
            return False
        finally:
            cur.close()
            conn.close()




    def main_run(self):

        url = "http://www.zhuzhu.cc/dh/index.html.bak"
        result = self.parseListHtml(url)
        print result
        #11 18,19,25,26
        for i in range(2,163):
            time.sleep(2)
            url = "http://www.zhuzhu.cc/dh/index" + str(i) + ".html"
            result = self.parseListHtml(url)
            print i,result


if __name__ == "__main__":
    app = Zhuzhudm()
    app.main_run()