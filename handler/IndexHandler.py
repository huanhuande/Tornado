__author__ = 'chengeng'
import tornado


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')