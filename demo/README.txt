flaskr 例子源码:
https://github.com/ajford/flask-wtf/tree/master/examples/flaskr
如何使用virtualenv安装
如何使用 wtf
如何使用一些类


关于如何使用virtualenv
http://www.cnblogs.com/cheungjustin/archive/2011/12/08/2281041.html

在window下面使用 virtualenv:
pip install virtualenv
然后建立一个环境
virtualenv --no-site-packages evn
cd evn\Scripts
activate.bat 是启动
deactivate.bat 是退出

写一个requirements.txt文件可以一次统一安装包
pip install -r requirements.txt