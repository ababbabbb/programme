from .connection import (
    BaseConnection,
    MySQLConnection,
    OracleConnection,
    SQLServerConnection,
    PostgresConnection,
    MongoDBConnection,
)
from utils import create_table

def get_connection(db_type, **kwargs):
    conn_cls = {
        'mysql': MySQLConnection,
        'oracle': OracleConnection,
        'sqlserver': SQLServerConnection,
        'postgres': PostgresConnection,
        'mongodb': MongoDBConnection,
    }.get(db_type)
    if conn_cls is None:
        raise ValueError(f'Unsupported database type: {db_type}')
    return conn_cls(**kwargs)