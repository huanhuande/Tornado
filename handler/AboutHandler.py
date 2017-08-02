__author__ = 'chengeng'
import tornado

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')
