import importlib
import os
import traceback

from boot_framework.Scanner.TargetBasic import BasicConfig, BeforeServlet, BackServlet
from boot_framework.ConfigContainer import configs, servlets_before, servlets_back


def scan_config(directory_path):
    for r, d, filenames in os.walk(directory_path):
        if 'mvc' not in r or 'config' not in r:
            continue
        for filename in filenames:
            if filename == '__init__.py' or not filename.endswith('.py'):
                continue

            try:
                module = importlib.machinery.SourceFileLoader(
                    filename.replace(',py', ''), os.path.join(r, filename)
                ).load_module()
                class_imported = getattr(module, filename.replace('.py', ''))
                if issubclass(class_imported, BasicConfig):
                    configs.append(class_imported)
            except Exception:
                print(traceback.format_exc())


def scan_servlet(directory_path):
    for r, d, filenames in os.walk(directory_path):
        if 'mvc' not in r or 'servlet' not in r:
            continue

        for filename in filenames:
            if filename == '__init__.py' or not filename.endswith('.py'):
                continue

            try:
                module = importlib.machinery.SourceFileLoader(
                    filename.replace(',py', ''), os.path.join(r, filename)
                ).load_module()

                class_imported = getattr(module, filename.replace('.py', ''))
                if issubclass(class_imported, BeforeServlet):
                    servlets_before.append(class_imported())
                if issubclass(class_imported, BackServlet):
                    servlets_back.append(class_imported())

            except Exception:
                print(traceback.format_exc())
