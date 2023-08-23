from flask_restful import Resource

from mvc.entity.vo.Response.response import my_response


class TestSysController(Resource):

    def get(self):

        return my_response('成功执行请求')
