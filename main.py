import os
import json
import asyncio
import uvloop

from os.path import join, dirname
from tornado import ioloop, web, template, httputil
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado_sqlalchemy import SQLAlchemy, SessionMixin, as_future
from typing import Any
from dotenv import load_dotenv
from models.sector import Sector


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
AsyncIOMainLoop().install()

class TemplateHandler(SessionMixin, web.RequestHandler):
    def __init__(self, application: "web.Application", request: httputil.HTTPServerRequest, **kwargs: Any) -> None:
        super().__init__(application, request, **kwargs)
        self.loader = template.Loader("templates/public")

    def get(self):
        self.write(self.loader.load("index.html").generate())

class SectorsHandler(SessionMixin, web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
        
    async def get(self):
        with self.make_session() as session:
            sectors = await as_future(session.query(Sector).all)
            session.commit()

        sectors = json.dumps([sector.as_dict() for sector in sectors])
        self.write(sectors)
    
    def put(self, *args, **kwargs) -> None:
        self.args = json.decode(self.request.body)
        print(self.request.body)

def routes():
    return web.Application([
        (r"/", TemplateHandler),
        (r"/sectors", SectorsHandler),
    ], db=SQLAlchemy(
        os.environ.get("DATABASE_URL"), 
        session_options={"expire_on_commit": False}))

if __name__ == "__main__":
    port = os.environ.get("PORT")
    try:
        app = routes()
        app.listen(port)
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt as e:
        print('Program exited')
