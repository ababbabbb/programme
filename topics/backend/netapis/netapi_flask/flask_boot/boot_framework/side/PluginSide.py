from typing import Any

from boot_framework.side.BasicSide import BasicSide


class PluginSide(BasicSide):

    @staticmethod
    def before(instance, *args, **kwargs):      # TODO：需要写出plugin系统，并传入实例对象及其参数
        ...

    @staticmethod
    def arbiter_around(instance, *args, **kwargs) -> bool:
        ...

        return False

    @staticmethod
    def around(instance, *args, **kwargs) -> Any:
        ...

    @staticmethod
    def after(instance, *args, **kwargs):
        ...

    @staticmethod
    def after_throwing(e, instance, *args, **kwargs) -> Any:
        ...
