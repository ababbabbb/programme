from flask import Flask

from boot_framework.AppFactory.basic import BasicFactory


class HttpFactory(BasicFactory):

    def __call__(self, name) -> Flask:
        self.app = Flask(name)

        return self.app

    def run(self, *args):
        ...
