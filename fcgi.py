#!/usr/bin/env python
from fkmv import create_app

app = create_app('config.cfg')

from flup.server.fcgi import WSGIServer
WSGIServer(app,bindAddress='/tmp/pypress-master.sock').run()
