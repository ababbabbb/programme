from ..connect import DBConnectionFactory


class Table:
    def __init__(self, db_type, db_name, table_name, **kwargs):
        self._db_type = db_type
        self._db_name = db_name
        self._table_name = table_name
        self._conn = DBConnectionFactory().create_connection(db_type, db_name, **kwargs)
    def create(self, fields):
        field_str = ", ".join([f"{field} {fields[field]}" for field in fields])
        sql = f"CREATE TABLE {self._table_name} ({field_str})"
        self._conn.execute(sql)
        self._conn.commit()
    def drop(self):
        sql = f"DROP TABLE IF EXISTS {self._table_name}"
        self._conn.execute(sql)
        self._conn.commit()
    def truncate(self):
        sql = f"TRUNCATE TABLE {self._table_name}"
        self._conn.execute(sql)
        self._conn.commit()
    def select(self, fields=None, limit=None, where=None):
        field_str = "*"
        if fields:
            field_str = ", ".join(fields)
        sql = f"SELECT {field_str} FROM {self._table_name}"
        if where:
            sql += f" WHERE {where}"
        if limit:
            sql += f" LIMIT {limit}"
        self._conn.execute(sql)
        return self._conn.fetchall()
    def insert(self, values):
        field_str = ", ".join(values.keys())
        value_str = ", ".join([f"'{value}'" for value in values.values()])
        sql = f"INSERT INTO {self._table_name} ({field_str}) VALUES ({value_str})"
        self._conn.execute(sql)
        self._conn.commit()
    def update(self, values, where=None):
        value_str = ", ".join([f"{field}='{value}'" for field, value in values.items()])
        sql = f"UPDATE {self._table_name} SET {value_str}"
        if where:
            sql += f" WHERE {where}"
        self._conn.execute(sql)
        self._conn.commit()
    def delete(self, where=None):
        sql = f"DELETE FROM {self._table_name}"
        if where:
            sql += f" WHERE {where}"
        self._conn.execute(sql)
        self._conn.commit()