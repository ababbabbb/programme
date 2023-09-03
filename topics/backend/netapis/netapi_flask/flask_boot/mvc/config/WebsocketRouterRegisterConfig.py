from flask_sockets import Sockets

from boot_framework.Scanner.TargetBasic import BasicConfig


class WebsocketRouterRegisterConfig(BasicConfig):
    sort = 1

    def init_app(self, app):
        pass
