这个目录主要放本地处理的火车头数据到MYSQL数据库内

suku结构
    表suku_page   放的是分类和列表页号,页号抓取列表
    表suku_mv   放的抓取的内容
    表suku_ls   播放列表

    suku.py 主要功能:
        处理初始suku_page 分类下有多少列表要页要抓取,然后抓取列表下的MV,然后插入数据库
        每次处理一个page里面的
    suku_update.py:
        每次处理一个更新之前抓取的MV,取得内容和列表
    suku_pub.py
        把抓取好的内容和列表分别更新suku_mv状态 和 把地址发布suku_ls里面
        每次处理一个




本地LINUXcrontab 环境：
*/2 * * * *  /usr/bin/python /home/ajaxj/www/fkmv/winapp/suku.py
*/3 * * * *  /usr/bin/python /home/ajaxj/www/fkmv/winapp/suku_update.py




 def readpage(self, id, url):

        url = self.url_base + url
        print id
        try:
            res = urllib2.urlopen(url, timeout=30)
            txt = res.read()
            #然后转码解析
            if re.search(r'gb2312', txt, re.I):
                txt = re.sub('gb2312', 'utf-8', txt)
                txt = txt.decode('gbk')
                soup = BeautifulSoup(txt.encode('utf-8'))
                div = soup.find('div', {'class': 'infobox border2 fl'})
                p_list = div.findAll('p')
                tp = p_list[0].string[5:]
                arts = p_list[1].string[5:]
                lang_ls = p_list[2].string.split('年份:'.decode('utf-8'))
                lang = lang_ls[0].strip()
                year = lang_ls[1]

                div = soup.find('div', {'class': 'videolist mb6'})
                lists = div

                # li_list = div.findAll("li")
                # lists = ''
                # for li in li_list:
                #     lists += str(li)


                div = soup.find('div', {'class': 'description mb6'})
                # p_list = div.findAll('p')
                # contents = ''
                # if len(p_list) > 0:
                #     for p in p_list:
                #         if p.string != None:
                #             contents += p.string
                # # print contents
                contents = div
                data = [id, lang, arts, year, contents, lists, tp]

                conn = psycopg2.connect(dbname="ajaxj", user="postgres", password="eeeeeeee")
                sql = "update mv_movie_zhuzhu set lang='%s',arts='%s',year='%s',contents='%s',lists='%s',tp='%s' where id=%d" % (
                data[1], data[2], data[3], data[4], data[5], data[6], int(data[0]))

                cur = conn.cursor()
                try:
                    cur.execute(sql)
                    conn.commit()
                except Exception, e:
                    print e
                    sys.exit(1)
                finally:
                    cur.close()
                    conn.close()

        except Exception, e:
            print e
            sys.exit(1)
