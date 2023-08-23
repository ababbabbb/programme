from abc import ABCMeta, abstractmethod


class BasicConfig(metaclass=ABCMeta):

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    @abstractmethod
    def init_app(self, app):
        # 实际上就是起到了配置类对应的配置内容加载效果
        ...


class BasicServlet(metaclass=ABCMeta):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        # 用于实现拦截器运行，必须实现
        ...


class BeforeServlet(BasicServlet):

    @abstractmethod
    def __call__(self, environ, start_response):
        ...


class BackServlet(BasicServlet):

    @abstractmethod
    def __call__(self, response):
        ...

