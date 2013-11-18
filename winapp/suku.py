# -*- coding:utf-8 -*-
import urllib2
import MySQLdb
import time
from BeautifulSoup import BeautifulSoup
import re


class Suku:
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
                _title = li.find('h5').text
                _cateen = "dongzuopian"
                _catecn = u"动作片"
                #
                result = self.insertListToDb(_title,_url,_cateen,_catecn)
                if result is False:
                    return False
            return True
        else:
            return False

    #插入列表页的MYSQL
    def insertListToDb(self,title,url,cateen,catecn):
        conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="3tv3",charset="utf8")
        sql = "SELECT * FROM suku_temp WHERE title = '%s'" %(title)
        cur = conn.cursor()
        cur.execute(sql)
        if cur.fetchone() == None:
            sql = "INSERT INTO suku_temp(title,url,cateen,catecn)" \
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

    def getListFormDb(self):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="3tv3",charset="utf8")
            sql = "SELECT * FROM suku_temp WHERE status = 0"
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchone()
            if data is not None:
                _url =  data[3]
                _url = 'http://www.suku.cc/film17/18997/'
                _html = self.readUrlToHtml(_url)
                if re.search(r'gb2312',_html,re.I):
                    html = re.sub('gb2312','utf-8',_html)
                    html = html.decode('gbk')
                soup = BeautifulSoup(html.encode('utf-8'))
                div = soup.find('div',{'class':'vodmain'})
                if div == None:
                    return False
                else:
                    p_list = div.findAll('p')
                    _banben = p_list[1].small.text.encode('utf-8').decode('utf-8')
                    print _banben[-1]
                    _arts = p_list[2].text.encode('utf-8').split('：')[1].decode('utf-8')
                    _location = p_list[5].text.encode('utf-8').split('：')[1].decode('utf-8')
                    _pubyear = p_list[6].text.encode('utf-8').split('：')[1].decode('utf-8')
                    _pubdate = p_list[7].text.encode('utf-8').split('：')[1].decode('utf-8')
                    #http://www.suku.cc//playdata/53/18997.js?81926.34
                _lists = ""
                div2 = soup.find('div',{'id':'v1'})
                if div2 != None:
                    _lists += str(div2)


                div2 = soup.find('div',{'id':'v2'})
                if div2 != None:
                    _lists +=str(div2)

                div3 = soup.find('div',{'class':'vod_content'})
                if div3 == None:
                    return  False
                else:
                    _contents =  div3.text.replace('\'','"')


            else:
                return False


            return True
        except Exception,e:
            print e
            return False
        finally:
            cur.close()
            conn.close()



if __name__ == '__main__':
    app = Suku()
    #print app.parseListHtml(app.url_dongzuo)
    print app.getListFormDb()