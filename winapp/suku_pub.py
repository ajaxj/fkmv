# -*-coding:utf-8 -*-
import re
import urllib2
import MySQLdb
from BeautifulSoup import BeautifulSoup
from xml.sax.saxutils import escape, unescape
#发布最后更新LIST表
class Sukupub:
    pwd = ""
    def parseList(self):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT id,list FROM suku_mv WHERE status = 1"
            cur = conn.cursor()
            cur.execute(sql)
            datalist = cur.fetchall()
            for data in datalist:
                soup = BeautifulSoup(data[1])
                a_list = soup.findAll("a")
                for a in a_list:
                    _txt = a.text
                    _url = a.get('href')
                    url = "http://www.suku.cc" + _url
                    req = urllib2.Request(url)
                    res = urllib2.urlopen(req,timeout=30)
                    _html = res.read()
                    if re.search(r'gb2312',_html,re.I):
                        html = re.sub('gb2312','utf-8',_html)
                        html = html.decode('gbk')

                    soup = BeautifulSoup(html)
                    div = soup.find('div',{'class':'player'})
                    url = "http://www.suku.cc" +  div.find('script').get('src')
                    req = urllib2.Request(url)
                    res = urllib2.urlopen(req,timeout=30)
                    _html = res.read()
                    _temp = _html.split('=unescape(\'')
                    _temp = _temp[1].split('\'')

                    sql = "SELECT * FROM suku_ls WHERE url = '%s'" %(_url)
                    cur.execute(sql)
                    if cur.fetchone() == None:
                        sql = "INSERT INTO suku_ls(mvid,txt,res,url) VALUES ('%d','%s','%s','%s')" %(int(data[0]),_txt,_temp[0],_url)
                        cur.execute(sql)
                        sql = "update suku_mv set status = 8 where id ='%d'" %(int(data[0]))
                        cur.execute(sql)
                        conn.commit()
                        print data[0],_txt,_url

        except Exception,e:
            print e
        finally:
            cur.close()
            conn.close()



if __name__ == '__main__':
    app = Sukupub()
    app.parseList()