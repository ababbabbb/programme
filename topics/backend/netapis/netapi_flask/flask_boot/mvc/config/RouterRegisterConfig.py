from flask_restful import Api

from boot_framework.Scanner.TargetBasic import BasicConfig


class RouterRegisterConfig(BasicConfig):

    def init_app(self, app):
        print('注册路由')
