
# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
import time
from BeautifulSoup import BeautifulSoup
import re



class Suku:
    pwd = "273511"
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
        conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
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

    #主程序 category 代表分类
    def main_run(self,category):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM suku_page WHERE status = 0 and category='%s'" %(category)
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchone()
            if data == None:
                return False
            url = "http://www.suku.cc/film17/index" + str(data[1]) +".html"
            result = self.parseListHtml(url)
            if result:
                sql = "update suku_page set status=1 where id=%d" %(int(data[0]))
                cur.execute(sql)
                conn.commit()
                return True
        except Exception,e:
            print e
            return False
        finally:
            cur.close()
            conn.close()



    def upDetail(self):
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
            sql = "SELECT * FROM suku_temp WHERE status = 0"
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchone()
            cur.close()
            conn.close()

            if data is not None:    #判断是否还有没有抓取更新的
                _id = data[0]
                _url =  data[3]
                #_url = 'http://www.suku.cc/film17/18997/'
                #_url = 'http://www.suku.cc/film17/7497/'
                #_url = 'http://www.suku.cc/film17/shisantaibao/'
                _html = self.readUrlToHtml(_url)

                if re.search(r'gb2312',_html,re.I):
                    html = re.sub('gb2312','utf-8',_html)
                    try:
                        html = html.decode('gbk')
                    except Exception,e:
                        #判断是否是码的问题,是的话变成status = 9
                        conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                        sql = "update suku_temp set status=9 where id=%d" %(int(_id))
                        cur = conn.cursor()
                        cur.execute(sql)
                        conn.commit()
                        return False
                soup = BeautifulSoup(html.encode('utf-8'))

                div = soup.find('div',{'class':'vodmain'})

                if div == None: #判断是否有内容
                    return False
                else:
                    p_list = div.findAll('p')

                    _banben = p_list[1].small.text.encode('utf-8').decode('utf-8')

                    if _banben[-1] == u"集" and _banben != u"全集":    #判断是否是连纽剧,是的话变成status = 2
                        try:
                            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                            sql = "update suku_temp set status=2 where id=%d" %(int(_id))
                            cur = conn.cursor()
                            cur.execute(sql)
                            conn.commit()
                            return False
                        except Exception,e:
                            print e
                            return False
                        finally:
                            cur.close()
                            conn.close()



                    else:

                        _img = p_list[0].find('img').get('src')
                        _arts = p_list[2].text.encode('utf-8').split('：')[1].decode('utf-8')
                        _location = p_list[5].text.encode('utf-8').split('：')[1].decode('utf-8')
                        _pubyear = p_list[6].text.encode('utf-8').split('：')[1].decode('utf-8')
                        _pubdate = p_list[7].text.encode('utf-8').split('：')[1].decode('utf-8')

                        _list = ""
                        div2 = soup.find('div',{'id':'v1'})
                        if div2 != None:
                            _list += div2.prettify().decode('utf-8')


                        div2 = soup.find('div',{'id':'v2'})
                        if div2 != None:
                            _list +=div2.prettify().decode('utf-8')

                        div3 = soup.find('div',{'class':'vod_content'})
                        if div3 == None:
                            return  False
                        else:
                            _content =  div3.text.replace('\'','"')



                        #更新
                        try:
                            conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                            sql = "update suku_temp set location='%s',pubdate='%s',arts='%s',pubyear='%s',content='%s',list='%s',img='%s',status=1 where id=%d" %(_location,_pubdate,_arts,_pubyear,_content,_list,_img,int(_id))
                            cur = conn.cursor()
                            cur.execute(sql)
                            conn.commit()
                            return True
                        except Exception,e:
                            print e
                            return False
                        finally:
                            cur.close()
                            conn.close()

            else:
                return False

        except Exception,e:
            print e
            return False

        return True




if __name__ == '__main__':
    app = Suku()
    app.upDetail()