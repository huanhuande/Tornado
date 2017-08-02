__author__ = 'chengeng'
import tornado

class WorkHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('work.html')