import inspect
import os


def get_a_file_path():
    frame = inspect.currentframe().f_back
    while frame:
        if frame.f_globals.get('__file__'):
            a_file_path = frame.f_globals['__file__']
            return os.path.abspath(a_file_path)
        frame = frame.f_back
