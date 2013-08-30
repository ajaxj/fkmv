# -*- coding:utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import sys

__author__ = 'Administrator'


#工具类
class Utils:

    def fetchHakuzyDetail(self,url):
        list = None
        try:
            res = urllib2.urlopen(url,timeout=30)
            html = res.read()
            soup = BeautifulSoup(html)
            table_list = soup.findAll('table')
            tb = table_list[5]
            trs = tb.findAll('tr')
            txt1 =  trs[0].find('strong').text
            txt2 = u'影片名称开始代码'
            txt3 =u'影片名称结束代码'
            txt =  trs[0].text
            _title =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[1].find('strong').text
            txt2 = u'影片副标开始代码'
            txt3 =u'影片副标结束代码'
            txt =  trs[1].text
            _banben =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[2].find('strong').text
            txt2 = u'影片演员开始代码'
            txt3 =u'影片演员结束代码'
            txt =  trs[2].text
            _arts =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[3].find('strong').text
            txt2 = u'影片导演开始代码'
            txt3 =u'影片导演结束代码'
            txt =  trs[3].text
            _dc =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[4].find('strong').text
            txt2 = u'影片类型开始代码'
            txt3 =u'影片类型结束代码'
            txt =  trs[4].text
            _category =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[5].find('strong').text
            txt2 = u'影片语言开始代码'
            txt3 =u'影片语言结束代码'
            txt =  trs[5].text
            _lang =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[6].find('strong').text
            txt2 = u'影片地区开始代码'
            txt3 =u'影片地区结束代码'
            txt =  trs[6].text
            _location =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[7].find('strong').text
            txt2 = u'影片更新时间开始代码'
            txt3 =u'影片更新时间结束代码'
            txt =  trs[7].text
            _pubdate =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt1 =  trs[8].find('strong').text
            txt2 = u'影片状态开始代码'
            txt3 =u'影片状态结束代码'
            txt =  trs[8].text
            _status =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'').replace('">','')

            txt1 =  trs[9].find('strong').text
            txt2 = u'上映日期开始代码'
            txt3 =u'上映日期结束代码'
            txt =  trs[9].text
            _year =  txt.replace(txt1,'').replace(txt2,'').replace(txt3,'')

            txt = trs[10].find('div').text
            txt2 = u'影片介绍开始代码'
            txt3 =u'影片介绍结束代码'
            _content =  txt.replace(txt2,'').replace(txt3,'')
            list = [_title,_banben,_arts,_dc,_category,_lang,_location,_pubdate,_status,_year,_content]

            # tb = table_list[7]
            # # inputs = tb.findAll('input')
            # # for input in inputs:
            # #     # print input.get('value')
            # #     print input.text
            # hrefs = tb.findAll('a')
            # for a in hrefs:
            #     print a.text

        except Exception,e:
            print e
            sys.exit(1)


        return list

