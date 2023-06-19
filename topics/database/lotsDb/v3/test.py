from . import DatabaseFactory, MySQLModel, OracleModel, \
    SQLServerModel, PostgreSQLModel, MongoDBModel


# 创建MySQL连接
mysql_factory = DatabaseFactory("mysql", "test_db", "localhost", 3306, "root", "password")
mysql_engine, mysql_session = mysql_factory.create_connection()
# 创建MySQL模型实例
mysql_model = MySQLModel(name="test")
mysql_model.save(mysql_session)
# 查询MySQL中的所有模型实例
mysql_models = MySQLModel.query_all(mysql_session)
for model in mysql_models:
    print(model.id, model.name)
# 创建Oracle连接
oracle_factory = DatabaseFactory("oracle", "test_db", "localhost", 1521, "system", "password")
oracle_engine, oracle_session = oracle_factory.create_connection()
# 创建Oracle模型实例
oracle_model = OracleModel(name="test")
oracle_model.save(oracle_session)
# 查询Oracle中的所有模型实例
oracle_models = OracleModel.query_all(oracle_session)
for model in oracle_models:
    print(model.id, model.name)
# 创建SQL Server连接
sql_server_factory = DatabaseFactory("sql_server", "test_db", "localhost", 1433, "sa", "password")
sql_server_engine, sql_server_session = sql_server_factory.create_connection()
# 创建SQL Server模型实例
sql_server_model = SQLServerModel(name="test")
sql_server_model.save(sql_server_session)
# 查询SQL Server中的所有模型实例
sql_server_models = SQLServerModel.query_all(sql_server_session)
for model in sql_server_models:
    print(model.id, model.name)
# 创建PostgreSQL连接
postgresql_factory = DatabaseFactory("postgresql", "test_db", "localhost", 5432, "postgres", "password")
postgresql_engine, postgresql_session = postgresql_factory.create_connection()
# 创建PostgreSQL模型实例
postgresql_model = PostgreSQLModel(name="test")
postgresql_model.save(postgresql_session)
# 查询PostgreSQL中的所有模型实例
postgresql_models = PostgreSQLModel.query_all(postgresql_session)
for model in postgresql_models:
    print(model.id, model.name)
# 创建MongoDB连接
mongodb_factory = DatabaseFactory("mongodb", "test_db", "localhost", 27017, "root", "password")
mongodb_db = mongodb_factory.create_connection()
# 创建MongoDB模型实例
mongodb_model = MongoDBModel(mongodb_db)
mongodb_model.save({"id": 1, "name": "test"})
# 查询MongoDB中的所有模型实例
mongodb_models = mongodb_model.query_all()
for model in mongodb_models:
    print(model)