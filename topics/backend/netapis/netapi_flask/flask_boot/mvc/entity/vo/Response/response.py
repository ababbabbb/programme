"""自定义response"""
from mvc.utils import stat


def my_response(message='成功', code=stat.OK, data=None):
    """自定义response"""
    response = {
        'code': code,
        'message': message,
        'data': data
    }
    if data is None:
        del response['data']
    return response
