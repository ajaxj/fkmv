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
    def parseHtml(self,html):
        #格式化utf-8
        if re.search(r'gb2312',html,re.I):
            html = re.sub('gb2312','utf-8',html)
            html = html.decode('gbk')

        soup = BeautifulSoup(html.encode('utf-8'))



