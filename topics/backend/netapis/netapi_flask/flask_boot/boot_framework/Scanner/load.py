from flask import Flask

from boot_framework.ConfigContainer import configs


def load_config(app: Flask):
    for config in configs:
        config(app)
