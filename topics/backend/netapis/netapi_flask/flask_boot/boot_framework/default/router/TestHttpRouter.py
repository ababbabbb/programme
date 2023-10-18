import importlib
import inspect
import os
import traceback

from functools import partial

from boot_framework.core.Basics.interaction import BasicHttpRouter
from boot_framework.side.TestSide import MethodTestSide


def scan_case(directory_path) -> dict:

    folder_pass = ['servlet', 'config', 'router', 'controller']
    for r, d, filenames in os.walk(directory_path):
        if 'mvc' not in r or any(r in folder for folder in folder_pass):
            continue

        for filename in filenames:
            if filename == '__init__.py' or not filename.endswith('.py'):
                continue

            try:
                module = importlib.machinery.SourceFileLoader(
                    filename.replace(',py', ''), os.path.join(r, filename)
                ).load_module()

                if MethodTestSide not in inspect.getmembers(module):
                    continue

                # 将所有的对象都实例化一次
                instances = [
                    cls[1](*cls[1].test_args) for cls in inspect.getmembers(module) if inspect.isclass(cls[1]) and any(
                        value for value in cls[1].__dict__.values() if isinstance(value, MethodTestSide)
                    )
                ]
                methods = [getattr(instance, m) for instance in instances for m in dir(instance) if
                           isinstance(getattr(instance, m), partial)]
                functions = [func for func in inspect.getmembers(module) if inspect.isfunction(func)]

                # TODO: 还需要动态创建controller类，并将其get方法替换为MethodTestSide.funcs中的方法

            except Exception:
                print(traceback.format_exc())

    return {'/'+key: value for key, value in MethodTestSide.funcs.items()}


class PluginHttpRouter(BasicHttpRouter):

    def register(self):

        self.dict_resource = scan_case(self.app.path_project)
        self.name_bp = __name__
        self.url_prefix = '/sys/side'
