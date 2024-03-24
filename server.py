import asyncio
import tornado
import os
import sys
import chat
import json


chatBot = None

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global chatBot
        chatBot = chat.ChatBot()
        self.render("index.html")

    def post(self):
        # passwd = self.get_argument("password")
        body = json.loads(self.request.body)
        print(body)
        human = body.get("human")
        print(human)
        result =  chatBot.invoke(human)
        print(result)
        # "Your username is %s and password is %s" % (body.get("username"), body.get("password"))
        self.write({'message': result.get('text')})

def make_app():
    settings = {
        'debug':True,
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        # "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        # "login_url": "/login",
        # "xsrf_cookies": True,
    }
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

async def main():
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Listening on port {port}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())


# class basicRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write(f"Hello served from {os.getpid()}")

# class queryStringRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         item = int(self.get_argument("item"))
#         self.write("Item is   " + item)        

# class staticRequestHanlder(tornado.web.RequestHandler):
#     def get(self):
#         self.render("index.html")

# if __name__ == "__main__":
    # app = tornado.web.Application([
    #     (r"/", basicRequestHandler),
    #     (r"/blog", staticRequestHanlder),
    #     (r"/queryTest", queryStringRequestHandler),
    #     # (r"/res/([0-9]+)", resourceRequestHandler)
    # ])

    # port = 3001
    # app.listen(port)
    # print(f"Listening on port {port}")
    # tornado.ioloop.IOLoop.current().start()