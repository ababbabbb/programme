"""
        db_manager.py: 数据库连接管理模块

        根据配置文件读取支持的数据库类型、主机地址、端口、用户名和密码等信息

        根据读取的配置信息，初始化数据库连接池

        提供获取数据库连接和ORM对象的方法

        实现单例模式，保证全局只有一个数据库连接池实例

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser


class DBManager:
    __instance = None

    def __init__(self):
        self.session = None

        if DBManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DBManager.__instance = self

    @staticmethod
    def get_instance():

        if DBManager.__instance == None:
            DBManager()
        return DBManager.__instance

    def init_engine(self, db_type, host, port, user, password, db_name):
        db_url = ''
        if db_type == 'mysql':
            db_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'
        elif db_type == 'oracle':
            db_url = f'oracle+cx_oracle://{user}:{password}@{host}:{port}/{db_name}'
        elif db_type == 'sql_server':
            db_url = f'mssql+pyodbc://{user}:{password}@{host}:{port}/{db_name}?driver=SQL+Server'
        elif db_type == 'postgresql':
            db_url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'
        elif db_type == 'mongodb':
            db_url = f'mongodb://{user}:{password}@{host}:{port}/{db_name}'
        else:
            raise ValueError(f"Unsupported db type {db_type}")

        engine = create_engine(db_url, pool_size=10, max_overflow=20, pool_recycle=60)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_session(self):

        return self.session

    def close_session(self):
        self.session.close()