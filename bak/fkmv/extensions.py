#!/usr/bin/env python
#coding=utf-8

#from flaskext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
#from flaskext.cache import Cache
#from flaskext.uploads import UploadSet, IMAGES

#__all__ = ['mail', 'db', 'cache', 'photos']
__all__ = ['db']
#mail = Mail()
db = SQLAlchemy()
#cache = Cache()
#photos = UploadSet('photos', IMAGES)

