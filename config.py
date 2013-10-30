#coding=utf8

DEBUG = True
FRAGMENT_PER_PAGE = 10

# -- Flask - SQLALCHEMY --
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
#server
MYSQL_USER = "admin"
MYSQL_PASS = "123456"
#local
#MYSQL_USER = 'root'
#MYSQL_PASS = ''
MYSQL_DB = 'ajaxj1'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
