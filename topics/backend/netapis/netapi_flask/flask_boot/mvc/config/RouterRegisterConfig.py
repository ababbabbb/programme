from flask_restful import Api

from boot_framework.BasicConfig import BasicConfig


class RouterRegisterConfig(BasicConfig):

    def init_app(self, app):
        print('注册路由')
