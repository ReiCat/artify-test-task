import os
import json
import asyncio
import uvloop

from os.path import join, dirname
from tornado import web, template, httputil
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado_sqlalchemy import SQLAlchemy, SessionMixin, as_future
from typing import Any
from dotenv import load_dotenv
from models.sector import Sector
from models.user import User


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
AsyncIOMainLoop().install()

class TemplateHandler(SessionMixin, web.RequestHandler):
    def __init__(self, application: "web.Application", request: httputil.HTTPServerRequest, **kwargs: Any) -> None:
        super().__init__(application, request, **kwargs)
        self.loader = template.Loader("templates/dist")

    def get(self):
        self.write(self.loader.load("index.html").generate())

class UserHandler(SessionMixin, web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
        
    async def get(self):
        with self.make_session() as session:
            user = await as_future(session.query(User).first)
        
        if not user:
            self.write(json.dumps({}))
            return
        user = json.dumps(user.as_dict())
        self.write(user)

    def post(self, *args, **kwargs) -> None:
        self.args = json.loads(self.request.body)
        user = User(name=self.args['name'], 
                    selected_sectors=str(self.args['selectedSectors']),
                    agreed_to_terms=self.args['isAgreed'])
        with self.make_session() as session:
            userInstance = session.get(User, 1)
            if userInstance:
                userInstance.name = user.name
                userInstance.selected_sectors = user.selected_sectors
                userInstance.agreed_to_terms = user.agreed_to_terms
            else:
                session.add(User)
            session.commit()
        user = json.dumps(userInstance.as_dict())
        self.write(user)

class SectorsHandler(SessionMixin, web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
        
    async def get(self):
        with self.make_session() as session:
            sectors = await as_future(session.query(Sector).all)
            session.commit()

        sectors = json.dumps([sector.as_dict() for sector in sectors])
        self.write(sectors)

class FormHandler(SessionMixin, web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')


def routes():
    return web.Application([
        (r"/", TemplateHandler),
        (r"/user", UserHandler),
        (r"/sectors", SectorsHandler),
        (r"/js/(.*)", web.StaticFileHandler, {'path': 'templates/dist/js/'})
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
