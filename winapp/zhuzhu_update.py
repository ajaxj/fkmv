
# -*- coding:utf-8 -*-

import urllib2
import MySQLdb

from BeautifulSoup import BeautifulSoup
import re
import time


class ZhuzhuUpdate:
    #pwd = "273511"
    pwd = ""


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


    #本地更新资料
    def upDetail(self,category):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM zhuzhu_mv WHERE status = 0 and cateen='%s'" %(category)
            cur = conn.cursor()
            cur.execute(sql)
            datalist = cur.fetchall()
            for data in datalist:
                _id = data[0]
                _url = "http://www.zhuzhu.cc" + data[3]
                _html = self.readUrlToHtml(_url)
                if re.search(r'gb2312',_html,re.I):
                    html = re.sub('gb2312','utf-8',_html)
                    try:
                        html = html.decode('gbk')
                    except Exception,e:
                        #判断是否是码的问题,是的话变成status = 9
                        #conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                        sql = "update zhuzhu_mv set status=9 where id=%d" %(int(_id))
                        #cur = conn.cursor()
                        cur.execute(sql)
                        conn.commit()

                else:
                    html = _html
                soup = BeautifulSoup(html.encode('utf-8'))
                div = soup.find('div', {'class': 'infobox border2 fl'})
                if div == None: #判断是否有内容
                    return False
                else:
                    p_list = div.findAll('p')
                    _arts = p_list[1].string[5:]
                    lang_ls = p_list[2].string.split('年份:'.decode('utf-8'))
                    _lang =  lang_ls[0].strip()
                    _pubyear = lang_ls[1]

                    _list = ""
                    div_list = soup.findAll('div', {'class': 'videolist mb6'})
                    for div in div_list:
                        _list += div.prettify().decode('utf-8')

                    div = soup.find('div', {'class': 'description mb6'})
                    _content =  div.find('ul').text.replace('\'','"')
                    sql = "update zhuzhu_mv set lang='%s',arts='%s',pubyear='%s',content='%s',list='%s',status=1 where id=%d" %( _lang,_arts,_pubyear,_content,_list,int(_id))
                    cur.execute(sql)
                    conn.commit()
                    print str(data[0]) + " " + data[3]
                    time.sleep(1)
        except Exception,e:
            return False
        finally:
            cur.close()
            conn.close()

    #一个临时的程式，把路径中的名字挖出来
    def upDetail2(self,category):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT id,url FROM zhuzhu_mv"
            cur = conn.cursor()
            cur.execute(sql)
            datalist = cur.fetchall()
            i = 0
            for data in datalist:
                _id = data[0]
                _url = data[1]
                _url_list = _url.split("/")
                _name =  _url_list[2].replace(".html","")
                sql = "UPDATE zhuzhu_mv set name='%s' where id = %d" %(_name,int(_id))
                cur.execute(sql)
                conn.commit()
                i += 1
                if i == 200:
                    print "sleep"
                    time.sleep(2)
                    i = 0
        except Exception,e:
            print e
        finally:
            cur.close()
            conn.close()







if __name__ == '__main__':
    app = ZhuzhuUpdate()
    app.upDetail2('dongzuopian')
    #app.upDetail("dongzuopian")
    #app.upDetail("xijupian")
    #app.upDetail("aiqingpian")
    #app.upDetail("kehuanpian")
    #app.upDetail("kongbupian")
    #app.upDetail("zhanzhengpian")
    #app.upDetail("juqingpian")