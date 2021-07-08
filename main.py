#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    port = int(os.environ.get('APP_PORT')) if os.environ.get('APP_PORT') else 8080;
    app = make_app()
    app.listen(port)
    print('Web server started at port ' + str(port));
    tornado.ioloop.IOLoop.current().start()
