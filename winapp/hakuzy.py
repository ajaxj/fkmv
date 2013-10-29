#!/usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb
import os
import win32com.client



# 插入火车头解析出来的list数据到MYSQL
def insertToMySQL(data):
    conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="ajaxj1",charset="utf8")
    sql = "SELECT * FROM hakuzy WHERE url= '%s' and catename ='%s'" %(data[1],data[0])
    cur = conn.cursor()
    cur.execute(sql)
    if cur.fetchone() == None:
        sql = "INSERT INTO hakuzy(catename,url,status) VALUES('%s','%s','%d')" %(data[0],data[1],data[2])
        try:
            cur.execute(sql)
            conn.commit()
        except Exception,e:
            print e
            exit(1)
        finally:
            cur.close()
            conn.close()


#从Access数据库读取数据,然后处理到MYSQL
# accessdb 本地access数据库地址 , catename 分类的名称
def getAccessToMySQL(accessdb = None,catename = 'dongzuopian'):
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source="+ accessdb +";"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            # 分类名,catename,远程地址,url,状态status
            data_list.append([catename,rs.Fields.Item(8).Value,0])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    for data in data_list:
        print data[1]
        insertToMySQL(data)


def main_run():
    # 火车头的数据库地址
    ## 动作片
    #AccessDB = "E:/LocoySpider/Data/LocoySpider/140/SpiderResult.mdb"
    #getAccessToMySQL(AccessDB,"dongzuopian")
    ##喜剧片 141
    #AccessDB = "E:/LocoySpider/Data/LocoySpider/141/SpiderResult.mdb"
    #getAccessToMySQL(AccessDB,"xijupian")
    ##战争片
    #AccessDB = "E:/LocoySpider/Data/LocoySpider/142/SpiderResult.mdb"
    #getAccessToMySQL(AccessDB,"zhanzhengpian")
    ##科幻片 143
    #AccessDB = "E:/LocoySpider/Data/LocoySpider/143/SpiderResult.mdb"
    #getAccessToMySQL(AccessDB,"kehuanpian")
    #爱情片 144
    AccessDB = "E:/LocoySpider/Data/LocoySpider/144/SpiderResult.mdb"
    getAccessToMySQL(AccessDB,"aiqingpian")
    #恐怖片 145
    AccessDB = "E:/LocoySpider/Data/LocoySpider/145/SpiderResult.mdb"
    getAccessToMySQL(AccessDB,"kongbupian")
    #剧情片 146
    AccessDB = "E:/LocoySpider/Data/LocoySpider/146/SpiderResult.mdb"
    getAccessToMySQL(AccessDB,"juqingpian")

if __name__ == "__main__":
    main_run()