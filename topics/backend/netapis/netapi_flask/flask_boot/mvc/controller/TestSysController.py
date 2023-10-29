from frame.conventions import BasicController
from mvc.entity.vo.Response.response import my_response


class TestSysController(BasicController):

    def get(self):

        return my_response('成功执行请求')
