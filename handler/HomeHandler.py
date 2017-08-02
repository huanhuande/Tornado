__author__ = 'chengeng'
import tornado

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')
