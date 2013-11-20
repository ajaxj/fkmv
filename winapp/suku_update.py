
# -*- coding:utf-8 -*-

import urllib2
import MySQLdb
import time
from BeautifulSoup import BeautifulSoup
import re



class SukuUpdate:
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
            sql = "SELECT * FROM suku_mv WHERE status = 0 and cateen='%s'" %(category)
            cur = conn.cursor()
            cur.execute(sql)
            datalist = cur.fetchall()
            for data in datalist:
                _id = data[0]
                _url =  data[3]
                _html = self.readUrlToHtml(_url)

                if re.search(r'gb2312',_html,re.I):
                    html = re.sub('gb2312','utf-8',_html)
                    try:
                        html = html.decode('gbk')
                    except Exception,e:
                        #判断是否是码的问题,是的话变成status = 9
                        #conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                        sql = "update suku_mv set status=9 where id=%d" %(int(_id))
                        #cur = conn.cursor()
                        cur.execute(sql)
                        conn.commit()
                        return False
                else:
                    html = _html
                soup = BeautifulSoup(html.encode('utf-8'))
                div = soup.find('div',{'class':'vodmain'})

                if div == None: #判断是否有内容
                    return False
                else:
                    p_list = div.findAll('p')
                    _banben = p_list[1].small.text.encode('utf-8').decode('utf-8')
                    if _banben[-1] == u"集" and _banben != u"全集":    #判断是否是连纽剧,是的话变成status = 2
                        try:
                            #conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                            sql = "update suku_mv set status=2 where id=%d" %(int(_id))
                            #cur = conn.cursor()
                            cur.execute(sql)
                            conn.commit()
                            #return False
                        except Exception,e:
                            print e
                            return False
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
                            #conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
                            sql = "update suku_mv set banben = '%s',location='%s',pubdate='%s',arts='%s',pubyear='%s',content='%s',list='%s',img='%s',status=1 where id=%d" %( _banben,_location,_pubdate,_arts,_pubyear,_content,_list,_img,int(_id))
                            #cur = conn.cursor()
                            cur.execute(sql)
                            conn.commit()
                            #return True
                        except Exception,e:
                            print e
                            #return False
                        #finally:
                        #    cur.close()
                        #    conn.close()

                        print str(data[0]) + " " + data[3]
        except Exception,e:
            print e
            return False
        finally:
            cur.close()
            conn.close()
        return True


    ## 服务器 更新资料
    #def upDetail(self):
    #    try:
    #        conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
    #        sql = "SELECT * FROM suku_temp WHERE status = 0"
    #        cur = conn.cursor()
    #        cur.execute(sql)
    #        data = cur.fetchone()
    #        cur.close()
    #        conn.close()
    #
    #        if data is not None:    #判断是否还有没有抓取更新的
    #            _id = data[0]
    #            _url =  data[3]
    #            _html = self.readUrlToHtml(_url)
    #
    #            if re.search(r'gb2312',_html,re.I):
    #                html = re.sub('gb2312','utf-8',_html)
    #                try:
    #                    html = html.decode('gbk')
    #                except Exception,e:
    #                    #判断是否是码的问题,是的话变成status = 9
    #                    conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
    #                    sql = "update suku_temp set status=9 where id=%d" %(int(_id))
    #                    cur = conn.cursor()
    #                    cur.execute(sql)
    #                    conn.commit()
    #                    return False
    #            soup = BeautifulSoup(html.encode('utf-8'))
    #            div = soup.find('div',{'class':'vodmain'})
    #
    #            if div == None: #判断是否有内容
    #                return False
    #            else:
    #                p_list = div.findAll('p')
    #
    #                _banben = p_list[1].small.text.encode('utf-8').decode('utf-8')
    #
    #                if _banben[-1] == u"集" and _banben != u"全集":    #判断是否是连纽剧,是的话变成status = 2
    #                    try:
    #                        conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
    #                        sql = "update suku_temp set status=2 where id=%d" %(int(_id))
    #                        cur = conn.cursor()
    #                        cur.execute(sql)
    #                        conn.commit()
    #                        return False
    #                    except Exception,e:
    #                        print e
    #                        return False
    #                    finally:
    #                        cur.close()
    #                        conn.close()
    #
    #                else:
    #
    #                    _img = p_list[0].find('img').get('src')
    #                    _arts = p_list[2].text.encode('utf-8').split('：')[1].decode('utf-8')
    #                    _location = p_list[5].text.encode('utf-8').split('：')[1].decode('utf-8')
    #                    _pubyear = p_list[6].text.encode('utf-8').split('：')[1].decode('utf-8')
    #                    _pubdate = p_list[7].text.encode('utf-8').split('：')[1].decode('utf-8')
    #
    #                    _list = ""
    #                    div2 = soup.find('div',{'id':'v1'})
    #                    if div2 != None:
    #                        _list += div2.prettify().decode('utf-8')
    #
    #                    div2 = soup.find('div',{'id':'v2'})
    #                    if div2 != None:
    #                        _list +=div2.prettify().decode('utf-8')
    #
    #                    div3 = soup.find('div',{'class':'vod_content'})
    #                    if div3 == None:
    #                        return  False
    #                    else:
    #                        _content =  div3.text.replace('\'','"')
    #
    #                    #更新
    #                    try:
    #                        conn = MySQLdb.connect(host="localhost",user="root",passwd=self.pwd,db="3tv3",charset="utf8")
    #                        sql = "update suku_temp set location='%s',pubdate='%s',arts='%s',pubyear='%s',content='%s',list='%s',img='%s',status=1 where id=%d" %(_location,_pubdate,_arts,_pubyear,_content,_list,_img,int(_id))
    #                        cur = conn.cursor()
    #                        cur.execute(sql)
    #                        conn.commit()
    #                        return True
    #                    except Exception,e:
    #                        print e
    #                        return False
    #                    finally:
    #                        cur.close()
    #                        conn.close()
    #
    #        else:
    #            return False
    #
    #    except Exception,e:
    #        print e
    #        return False
    #
    #    return True




if __name__ == '__main__':
    app = SukuUpdate()
    app.upDetail("dongzuopian")