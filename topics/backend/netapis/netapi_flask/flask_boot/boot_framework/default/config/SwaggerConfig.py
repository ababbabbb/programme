from flask import Flask
from flasgger import Swagger

from boot_framework.core.Basics import BasicConfig


class SwaggerConfig(BasicConfig):
    swagger = None

    def init_app(self, app: Flask):
        self.swagger = Swagger()
        self.swagger.init_app(app)
