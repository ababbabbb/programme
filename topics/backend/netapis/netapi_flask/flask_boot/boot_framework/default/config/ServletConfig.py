from flask import Flask

from boot_framework.core.Basics import BasicConfig
from boot_framework.core.servlet.BootMiddleWare import BootMiddleware


class ServletConfig(BasicConfig):

    def init_app(self, app: Flask):
        app.wsgi_app = BootMiddleware(app.wsgi_app)
