import os
import typing as t
from typing import Optional

from flask import Flask

from boot_framework.Scanner.scan import scan_config, scan_servlet
from boot_framework.Scanner.load import load_config


class BootFrame:

    def __init__(self):
        self.app: Optional[None, Flask] = None

        self.path_dir_code = None

    def init_frame(self):
        self._scan()
        self._load()

        return self

    def _scan(self):
        scan_config(self.path_dir_code)  # 配置初始化
        scan_servlet(self.path_dir_code)

    def _load(self):
        load_config(self.app)

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
