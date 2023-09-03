from abc import ABCMeta, abstractmethod
from typing import Optional, Dict, Type, TypeVar

from flask import Blueprint
from flask_restful import Resource, Api

T = TypeVar('T', bound=Resource)


class BasicConfig(metaclass=ABCMeta):
    sort: Optional[int] = None

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    @abstractmethod
    def init_app(self, app):
        # 实际上就是达到了配置类对应的配置内容加载效果
        ...


class BasicHttpRouter(metaclass=ABCMeta):

    def __init__(self, app=None):
        self.app = app
        self.dict_resource: Optional[Dict[str, Type[T]]] = None
        self.name_bp: Optional[str] = None
        self.url_prefix: Optional[str] = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.register()
        self.bind()

    def bind(self):
        if not self.dict_resource or not self.name_bp or not self.url_prefix:
            raise ValueError('name_bp、url_prefix、dict_resource cannot be None')

        if '/' not in self.url_prefix:
            raise ValueError('url_prefix must contain \'/\'')

        blueprint = Blueprint(self.name_bp, __name__, url_prefix=self.url_prefix)
        api = Api(blueprint)

        for url, resource_cls in self.dict_resource.items():
            api.add_resource(resource_cls, url)

        self.app.register_blueprint(blueprint, url_prefix=self.url_prefix)

    @abstractmethod
    def register(self):
        ...


class BasicServlet(metaclass=ABCMeta):
    sort: Optional[int] = None

    @abstractmethod
    def __call__(self, *args, **kwargs):
        # 用于实现拦截器运行，必须实现
        ...


class OutContextBeforeServlet(BasicServlet):

    @abstractmethod
    def __call__(self, environ, start_response):
        ...


class OutContextBackServlet(BasicServlet):

    @abstractmethod
    def __call__(self, response):
        ...


class BeforeServlet(BasicServlet):

    @abstractmethod
    def __call__(self):
        ...


class BackServlet(BasicServlet):

    @abstractmethod
    def __call__(self, response):
        ...
