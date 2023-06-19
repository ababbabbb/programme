import psycopg2

from model import Field, Model, IntegerField, StringField
from options import Filter, Validator
from connect import DBConnection


class FloatField(Field):
    """
        添加新字段类型
    """
    def to_sql(self):

        return f"{self._field_name} FLOAT"


class Person(Model):
    id = IntegerField("mysql", "testdb", "id")
    name = StringField("mysql", "testdb", "name")
    age = IntegerField("mysql", "testdb", "age")
    height = FloatField("mysql", "testdb", "height")


class StartsWithFilter(Filter):
    """
        添加新数据过滤器
    """
    def apply(self, data):
        return {item for item in data if item[self._field].startswith(self._value)}


class EmailValidator(Validator):
    """
        添加新数据校验器
    """
    def validate(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format")


class PostgreSQLConnection(DBConnection):
    def __init__(self, db_name, **kwargs):
        super().__init__(db_name, **kwargs)
        conn_str = f"dbname='{db_name}' user='{kwargs['user']}' password='{kwargs['password']}' host='{kwargs['host']}' port='{kwargs['port']}'"
        self._conn = psycopg2.connect(conn_str)
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
