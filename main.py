__author__ ="huanfuan"

import os.path
import random

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from handler.IndexHandler import IndexHandler
from handler.HomeHandler import HomeHandler
from handler.WorkHandler import WorkHandler
from handler.AboutHandler import AboutHandler
from handler.ContactHandler import ContactHandler


from tornado.options import define, options
define("port", default=8083, help="run on the given port", type=int)

# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('index.html')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/about', AboutHandler),
            (r'/home', HomeHandler),
            (r'/work', WorkHandler),
            (r'/contact', ContactHandler),


        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()