class DBConnection:
    def __init__(self, db_name, **kwargs):
        self._db_name = db_name
    def execute(self, sql):
        raise NotImplementedError
    def commit(self):
        raise NotImplementedError
    def rollback(self):
        raise NotImplementedError
    def close(self):
        raise NotImplementedError