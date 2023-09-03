import os
import typing as t
from typing import Optional

from flask import Flask

from boot_framework.Scanner.scan import scan_config, scan_servlet, scan_servlet_out_context, scan_router_http
from boot_framework.Scanner.load import load_config, load_router_http, load_servlet
from boot_framework.default.Exception.handler import handle_exception
from boot_framework.default.Exception.Exceptions import BootException
from boot_framework.default.config.ServletConfig import ServletConfig
from boot_framework.ConfigContainer import configs

configs.append(ServletConfig)


class BootFrame:

    def __init__(self):
        self.app: Optional[None, Flask] = None

        self.path_dir_code = None

    def init_frame(self):
        self._load_config()     # 这顺序有讲究的，不能乱改，尤其config和router之间的顺序，跟wsgi_app有关
        self._load_servlet_out_context()
        self._load_servlet()
        self._load_router_http()
        self.app.errorhandler(BootException)(handle_exception)

        return self

    def _load_config(self):
        scan_config(self.path_dir_code)  # 配置初始化
        load_config(self.app)

    def _load_servlet_out_context(self):
        scan_servlet_out_context(self.path_dir_code)

    def _load_servlet(self):
        scan_servlet(self.path_dir_code)
        load_servlet(self.app)

    def _load_router_http(self):
        scan_router_http(self.path_dir_code)
        load_router_http(self.app)

    def run(
            self,
            host: t.Optional[str] = None,
            port: t.Optional[int] = None,
            debug: t.Optional[bool] = None,
            load_dotenv: bool = True,
            **options: t.Any,
    ) -> None:
        self.app.run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

    def __call__(self, name, path):
        self.app = Flask(name)
        self.path_dir_code = os.path.abspath(path).replace('main.py', '')

        return self


Frame = BootFrame()


__all__ = [
    'Frame'
]
