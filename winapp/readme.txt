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

