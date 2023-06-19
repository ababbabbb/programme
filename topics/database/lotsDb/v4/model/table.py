from ..connect import DBConnectionFactory
from field import Field
from ..options.table import Table


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        for key in fields.keys():
            attrs.pop(key)
        attrs["_fields"] = fields
        attrs["_table_name"] = name.lower()
        return super().__new__(cls, name, bases, attrs)
class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        self._data = {}
        for field in self._fields.values():
            self._data[field._field_name] = kwargs.get(field._field_name, None)
    def __getattr__(self, name):
        if name in self._fields:
            return self._data.get(name, None)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    def __setattr__(self, name, value):
        if name in self._fields:
            field = self._fields[name]
            if value is not None:
                field.validate(value)
            self._data[name] = value
        else:
            super().__setattr__(name, value)
    def save(self):
        fields = []
        values = []
        for field in self._fields.values():
            if self._data[field._field_name] is not None:
                fields.append(field._field_name)
                values.append(self._data[field._field_name])
        if len(fields) == 0:
            return
        field_str = ", ".join(fields)
        value_str = ", ".join([f"'{value}'" for value in values])
        sql = f"INSERT INTO {self._table_name} ({field_str}) VALUES ({value_str})"
        conn = DBConnectionFactory().create_connection(self._db_type, self._db_name)
        conn.execute(sql)
        conn.commit()
    @classmethod
    def create_table(cls, db_type, db_name, **kwargs):
        fields = []
        for field in cls._fields.values():
            fields.append(field.to_sql())
        field_str = ", ".join(fields)
        sql = f"CREATE TABLE {cls._table_name} ({field_str})"
        conn = DBConnectionFactory().create_connection(db_type, db_name, **kwargs)
        conn.execute(sql)
        conn.commit()
    @classmethod
    def drop_table(cls, db_type, db_name, **kwargs):
        sql = f"DROP TABLE IF EXISTS {cls._table_name}"
        conn = DBConnectionFactory().create_connection(db_type, db_name, **kwargs)
        conn.execute(sql)
        conn.commit()
    @classmethod
    def select(cls, db_type, db_name, fields=None, limit=None, where=None, **kwargs):
        table = Table(db_type, db_name, cls._table_name, **kwargs)
        data = table.select(fields, limit, where)
        return [cls(**item) for item in data]
    @classmethod
    def delete(cls, db_type, db_name, where=None, **kwargs):
        table = Table(db_type, db_name, cls._table_name, **kwargs)
        table.delete(where)
    @classmethod
    def truncate(cls, db_type, db_name, **kwargs):
        table = Table(db_type, db_name, cls._table_name, **kwargs)
        table.truncate()