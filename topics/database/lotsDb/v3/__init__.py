from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pymongo import MongoClient


class DatabaseFactory:
    """工厂类，用于创建数据库连接和会话"""

    def __init__(self, db_type, db_name, db_host, db_port, db_user, db_password):
        self.db_type = db_type
        self.db_name = db_name
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password

    def create_connection(self):
        if self.db_type == "mysql":
            engine = create_engine(
                f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        elif self.db_type == "oracle":
            engine = create_engine(
                f"oracle://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        elif self.db_type == "sql_server":
            engine = create_engine(
                f"mssql+pymssql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        elif self.db_type == "postgresql":
            engine = create_engine(
                f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        elif self.db_type == "mongodb":
            client = MongoClient(host=self.db_host, port=self.db_port, username=self.db_user, password=self.db_password)
            return client[self.db_name]
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

        Session = sessionmaker(bind=engine)
        session = Session()

        return engine, session


class BaseMixin:
    """ORM mixin类，提供常见的增删改查操作"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    @classmethod
    def query_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def query_by_id(cls, session, id_):
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def query_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).first()


Base = declarative_base()


class MySQLModel(Base, BaseMixin):
    """MySQL数据库中的模型"""
    __tablename__ = "mysql_model"


class OracleModel(Base, BaseMixin):
    """Oracle数据库中的模型"""
    __tablename__ = "oracle_model"


class SQLServerModel(Base, BaseMixin):
    """SQL Server数据库中的模型"""
    __tablename__ = "sqlserver_model"


class PostgreSQLModel(Base, BaseMixin):
    """PostgreSQL数据库中的模型"""
    __tablename__ = "postgresql_model"


class MongoDBModel:
    """MongoDB数据库中的模型"""

    def __init__(self, db):
        self.collection = db["mongodb_model"]

    def save(self, document):
        self.collection.insert_one(document)

    def delete(self, document):
        self.collection.delete_one(document)

    def query_all(self):
        return self.collection.find()

    def query_by_id(self, id_):
        return self.collection.find_one({"id": id_})

    def query_by_name(self, name):
        return self.collection.find_one({"name": name})