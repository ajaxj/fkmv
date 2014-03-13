#coding=utf8

DEBUG = True
FRAGMENT_PER_PAGE = 10

# -- Flask - SQLALCHEMY --
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
#server
MYSQL_USER = "root"
# MYSQL_PASS = "eeeeeeee"
#local
#MYSQL_USER = 'root'
MYSQL_PASS = ''
MYSQL_DB = '3tv3'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
