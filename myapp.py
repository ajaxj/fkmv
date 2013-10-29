#coding=utf8

# import sys
# import os
# abspath = os.path.abspath(__file__)
# app_root = os.path.dirname(abspath)
# path = os.path.join(app_root, 'virtualenv.bundle')
# sys.path.insert(0, path)
# sys.path.insert(0, app_root)


from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
from views import *

if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0')