这个目录主要放本地处理的火车头数据到MYSQL数据库内


xj-Lenovo-Product:~/www/fkmv/winapp$ python suku.py

*/2 * * * *  /usr/bin/python /home/ajaxj/www/fkmv/winapp/suku.py

def fetchmovie_by_url_category(self,url,category):

        data_list = []
        try:
            res = urllib2.urlopen(url,timeout=30)
            txt = res.read()
            if re.search(r'gb2312',txt,re.I):
                txt = re.sub('gb2312','utf-8',txt)
                txt = txt.decode('gbk')
            soup = BeautifulSoup(txt.encode('utf-8'))
            #查找所有相关MV的DIV
            ul = soup.find('ul',{'class':'img-list'})
            li_list = ul.findAll('li')
            for li in li_list:
                _title = li.find('img').get('alt').replace('\'',' ')
                _url = li.find('a').get('href')
                _img = li.find('img').get('src')
                sStr1 = li.findAll('a')[0].text
                _status = sStr1
                _category = category
                data_list.append([_title,_url,_img,_category,_status])
        except socket.error:
            errno,errstr = sys.exc_info()[:2]
            if errno == socket.timeout:
                print errstr
            sys.exit(1)
        return data_list


 if re.search(r'gb2312',txt,re.I):
                txt = re.sub('gb2312','utf-8',txt)
                txt = txt.decode('gbk')
            soup = BeautifulSoup(txt.encode('utf-8'))
            div1 = soup.find('div',{'class':'vodmain'})
            if div1 == None:
                exit(1)

            p_list = div1.findAll('p')
            _arts = p_list[2].text.encode('utf-8').split('：')[1].decode('utf-8')
            _tp = p_list[4].text.encode('utf-8').split('：')[1].decode('utf-8')
            _location = p_list[5].text.encode('utf-8').split('：')[1].decode('utf-8')
            _year = p_list[6].text.encode('utf-8').split('：')[1].decode('utf-8')
            _pubdate = p_list[7].text.encode('utf-8').split('：')[1].decode('utf-8')

            _lists = ""
            div2 = soup.find('div',{'id':'v1'})
            if div2 != None:
                _lists += str(div2)


            div2 = soup.find('div',{'id':'v2'})
            if div2 != None:
                _lists +=str(div2)


            div3 = soup.find('div',{'class':'vod_content'})
            if div3 == None:
                exit(1)
            _contents =  div3.text.replace('\'','"')

            conn =  MySQLdb.connect(host="localhost",user="root",passwd="",db="ajaxj",charset="utf8")
            sql = "update mv_movie_suku set location='%s',pubdate='%s',arts='%s',year='%s',contents='%s',lists='%s',tp='%s',ck=1 where id=%d" %(_location,_pubdate,_arts,_year,_contents,_lists,_tp,int(id))

            cur = conn.cursor()
            try:
                cur.execute(sql)
                conn.commit()
            except Exception,e:
                print e
                sys.exit(1)
            finally:
                cur.close()
                conn.close()

        except Exception,e:
            print e
            sys.exit(1)
