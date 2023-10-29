from flask import Flask

from frame.AppFactory.basic import BasicFactory


class HttpFactory(BasicFactory):

    def __call__(self, name) -> Flask:
        self.app = Flask(name)

        return self.app

    def run(self, *args):
        ...
