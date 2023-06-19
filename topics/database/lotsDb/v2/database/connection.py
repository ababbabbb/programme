import mysql.connector


class BaseConnection:
    def __init__(self, **kwargs):
        self._conn = None

    def connect(self):
        raise NotImplementedError

    def close(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def execute(self, sql, params=None):
        raise NotImplementedError

    def fetchall(self):
        raise NotImplementedError

    def fetchone(self):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError


class MySQLConnection(BaseConnection):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._conn = mysql.connector.connect(**kwargs)
        self._cursor = self._conn.cursor()
    def connect(self):
        if self._conn is None:
            self._conn = mysql.connector.connect(**kwargs)
            self._cursor = self._conn.cursor()
    def execute(self, sql, params=None):
        self._cursor.execute(sql, params)
    def fetchall(self):
        return self._cursor.fetchall()
    def fetchone(self):
        return self._cursor.fetchone()
    def commit(self):
        self._conn.commit()
    def rollback(self):
        self._conn.rollback()