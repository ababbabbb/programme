import os
from typing import Optional

from flask import Flask

from boot_framework.ConfigScanner import scan_config


class FrameInit:

    def __init__(self):
        self.app: Optional[None, Flask] = None

        self.path_dir_code = None

    def init_frame(self):
        scan_config(self.path_dir_code, self.app)  # 配置初始化

        return self

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    def __call__(self, name, path):
        self.app = Flask(name)
        self.path_dir_code = os.path.abspath(path).replace('main.py', '')

        return self


Frame = FrameInit()


__all__ = [
    'Frame'
]
