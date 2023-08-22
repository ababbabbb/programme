from flask import Flask

from boot_framework.Scanner.TargetBasic import BasicConfig
from boot_framework.default.servlet.BootMiddleware import BootMiddleware


class ServletConfig(BasicConfig):

    def init_app(self, app: Flask):
        app.wsgi_app = BootMiddleware(app.wsgi_app)
