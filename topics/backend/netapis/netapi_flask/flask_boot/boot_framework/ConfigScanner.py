import importlib
import os
import traceback

from boot_framework.BasicConfig import BasicConfig


def scan_config(directory_path, app):
    for r, d, filenames in os.walk(directory_path):
        if 'mvc' not in r:
            continue
        for filename in filenames:
            if filename.endswith("Config.py"):
                try:
                    module = importlib.machinery.SourceFileLoader(
                        filename.replace(',py', ''), os.path.join(r, filename)
                    ).load_module()
                    class_imported = getattr(module, filename.replace('.py', ''))
                    if issubclass(class_imported, BasicConfig):
                        class_imported(app)
                except Exception:
                    print(traceback.format_exc())
