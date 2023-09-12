from flask import Blueprint
from flask_restful import Resource, Api
from typing import Optional, Dict, Type, TypeVar

from abc import ABCMeta, abstractmethod


T = TypeVar('T', bound=Resource)


class BasicInteraction(metaclass=ABCMeta):
    """
    交互层基类
    """

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    @abstractmethod
    def init_app(self, app):
        ...


class BasicHttpRouter(BasicInteraction):
    """
    交互层下的http路由交互基类
    """

    def __init__(self, app=None):
        self.dict_resource: Optional[Dict[str, Type[T]]] = None
        self.name_bp: Optional[str] = None
        self.url_prefix: Optional[str] = None
        super().__init__(app)

    def init_app(self, app):
        self.register()
        self.bind()

    def bind(self):
        if not self.dict_resource or not self.name_bp or not self.url_prefix:
            raise ValueError('name_bp、url_prefix、dict_resource cannot be None')

        if '/' not in self.url_prefix:
            raise ValueError('url_prefix must contain \'/\'')

        blueprint = Blueprint(self.name_bp.replace('.py', ''), __name__, url_prefix=self.url_prefix)
        api = Api(blueprint)

        for url, resource_cls in self.dict_resource.items():
            api.add_resource(resource_cls, url)

        self.app.register_blueprint(blueprint, url_prefix=self.url_prefix)

    @abstractmethod
    def register(self):
        ...
