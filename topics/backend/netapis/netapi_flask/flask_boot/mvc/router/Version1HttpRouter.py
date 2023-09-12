from boot_framework.conventions import BasicHttpRouter

version = '1'


class Version1HttpRouter(BasicHttpRouter):

    def register(self):
        from mvc.controller.TestSysController import TestSysController

        self.dict_resource = {
            '/sys': TestSysController
        }
        self.name_bp = __name__
        self.url_prefix = '/api/test/v{0}'.format(version)
