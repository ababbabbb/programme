from abc import ABCMeta, abstractmethod


class BasicConfig(metaclass=ABCMeta):

    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    @abstractmethod
    def init_app(self, app):
        ...
