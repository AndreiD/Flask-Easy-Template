#!/usr/bin/python
# -*- coding: utf-8 -*-

import tornado
from tornado import autoreload
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from application import app

enable_pretty_logging()

PORT = 5000

# ------- PRODUCTION CONFIG -------
# http_server = HTTPServer(WSGIContainer(app))
# http_server.bind(PORT)
# http_server.start(0)
# ioloop = tornado.ioloop.IOLoop().instance()
# autoreload.start(ioloop)
# ioloop.start()


# ------- DEVELOPMENT CONFIG -------
app.run(port=PORT, debug=True)
