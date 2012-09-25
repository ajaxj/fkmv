
	
配置文件名是 config.cfg

使用flask.ext.script 脚本扩展

同步数据库命令
python manage.py createall
运行服务器命令
python manage.py runserver

初始数据
Admin:
	python manage.py createcode -r admin

Create three members in a batch:
	
	python manage.py createcode -r member -n 3

###Signup
	
	http://localhost:8080/account/signup/
