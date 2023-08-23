from flask import Blueprint, Flask
from flask_restful import Api

from boot_framework.Scanner.TargetBasic import BasicConfig
from mvc.controller.TestSysController import TestSysController

version = '1'


class RouterRegisterConfig(BasicConfig):
    version_bp = Blueprint('v{0}'.format(version), __name__)
    api: Api = None

    def init_app(self, app: Flask):
        self.register()

        app.register_blueprint(self.version_bp, url_prefix='/api/test/v{0}'.format(version))

    def register(self):
        self.api = Api(self.version_bp)

        # TODO: url的绑定、管理应该放到外部
        self.api.add_resource(TestSysController, '/sys')
