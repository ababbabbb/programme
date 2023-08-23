

class BootException(Exception):
    def __init__(self, msg: str, code: int):
        self.msg = msg
        self.code = code

    def __str__(self):

        return self.msg
