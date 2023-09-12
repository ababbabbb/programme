from typing import Type, TypeVar, Optional

from flask_restful import Resource

from boot_framework.core.Basics.serializer import BasicSerializer


T = TypeVar('T', bound=BasicSerializer)


class BasicController(Resource):
    serializer_class: Optional[Type[T]] = None
    decorators_get = []
    decorators_post = []
    decorators_put = []
    decorators_patch = []
    decorators_delete = []

    method_decorators = {
        'get': decorators_get,
        'post': decorators_post,
        'put': decorators_put,
        'patch': decorators_patch,
        'delete': decorators_delete
    }
