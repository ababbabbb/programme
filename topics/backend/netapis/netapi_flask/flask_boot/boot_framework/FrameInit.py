import os

from flask import Flask

from boot_framework.ConfigScanner import scan_config


class FrameInit:

    def __init__(self, name, path):
        self.app = Flask(name)

        self.path_dir_code = os.path.abspath(path).replace('main.py', '')

    def init_frame(self):
        scan_config(self.path_dir_code, self.app)  # 配置初始化

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
