#!/usr/bin/python
#-*- coding: utf-8 -*-

import tornado
from tornado import autoreload
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging

from app import app


enable_pretty_logging()


# ------- for production use this one --------->
# http_server = HTTPServer(WSGIContainer(app))
# http_server.bind(1337)
# http_server.start(0)
# ioloop = tornado.ioloop.IOLoop().instance()
# autoreload.start(ioloop)
# ioloop.start()



#------- for debugging use this one --------->
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
ioloop = tornado.ioloop.IOLoop().instance()
autoreload.start(ioloop)
ioloop.start()
