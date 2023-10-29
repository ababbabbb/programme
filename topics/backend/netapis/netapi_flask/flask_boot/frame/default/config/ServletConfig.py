from flask import Flask

from frame.core.Basics import BasicConfig
from frame.core.servlet.BootMiddleWare import BootMiddleware


class ServletConfig(BasicConfig):

    def init_app(self, app: Flask):
        app.wsgi_app = BootMiddleware(app.wsgi_app)
