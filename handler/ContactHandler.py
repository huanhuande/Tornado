__author__ = 'chengeng'
import tornado

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('contact.html')
