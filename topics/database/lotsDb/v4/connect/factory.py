class DBConnectionFactory:
    def __init__(self):
        self._connections = {}
    def create_connection(self, db_type, db_name, **kwargs):
        key = (db_type, db_name)
        if key not in self._connections:
            if db_type == "mysql":
                self._connections[key] = MySQLConnection(db_name, **kwargs)
            elif db_type == "sqlserver":
                self._connections[key] = SQLServerConnection(db_name, **kwargs)
            elif db_type == "oracle":
                self._connections[key] = OracleConnection(db_name, **kwargs)
        return self._connections[key]