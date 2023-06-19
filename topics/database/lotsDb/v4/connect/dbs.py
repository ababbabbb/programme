import dbs.connector
import pyodbc
import cx_Oracle

from base import DBConnection


class MySQLConnection(DBConnection):
    def __init__(self, db_name, **kwargs):
        super().__init__(db_name, **kwargs)
        self._conn = mysql.connector.connect(database=db_name, **kwargs)
        self._cursor = self._conn.cursor()
    def execute(self, sql):
        self._cursor.execute(sql)
    def commit(self):
        self._conn.commit()
    def rollback(self):
        self._conn.rollback()
    def close(self):
        self._cursor.close()
        self._conn.close()


class SQLServerConnection(DBConnection):
    def __init__(self, db_name, **kwargs):
        super().__init__(db_name, **kwargs)
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={kwargs['server']};DATABASE={db_name};UID={kwargs['user']};PWD={kwargs['password']}"
        self._conn = pyodbc.connect(conn_str)
        self._cursor = self._conn.cursor()
    def execute(self, sql):
        self._cursor.execute(sql)
    def commit(self):
        self._conn.commit()
    def rollback(self):
        self._conn.rollback()
    def close(self):
        self._cursor.close()
        self._conn.close()


class OracleConnection(DBConnection):
    def __init__(self, db_name, **kwargs):
        super().__init__(db_name, **kwargs)
        conn_str = f"{kwargs['user']}/{kwargs['password']}@{kwargs['host']}:{kwargs['port']}/{db_name}"
        self._conn = cx_Oracle.connect(conn_str)
        self._cursor = self._conn.cursor()
    def execute(self, sql):
        self._cursor.execute(sql)
    def commit(self):
        self._conn.commit()
    def rollback(self):
        self._conn.rollback()
    def close(self):
        self._cursor.close()
        self._conn.close()
