import traceback
from typing import Any
import functools
from abc import ABCMeta, abstractmethod

from boot_framework.core.Exception.Exceptions import BootException


class BasicSide(metaclass=ABCMeta):

    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return functools.partial(self, instance)

    @staticmethod
    @abstractmethod
    def before(instance, *args, **kwargs):
        ...

    @staticmethod
    @abstractmethod
    def arbiter_around(instance, *args, **kwargs) -> bool:
        ...

        return False

    @staticmethod
    @abstractmethod
    def around(instance, *args, **kwargs) -> Any:
        ...

    @staticmethod
    @abstractmethod
    def after(instance, *args, **kwargs):
        ...

    @staticmethod
    @abstractmethod
    def after_throwing(e, instance, *args, **kwargs) -> Any:
        ...

    def __call__(self, *args, **kwargs):

        try:
            self.before(*args, **kwargs)
            if self.arbiter_around(*args, **kwargs):
                ret = self.around(*args, **kwargs)
            else:
                ret = self.func(*args, **kwargs)
            self.after(*args, **kwargs)
        except BootException:
            raise
        except Exception:
            ret = self.after_throwing(traceback.format_exc(), *args, **kwargs)

        return ret
