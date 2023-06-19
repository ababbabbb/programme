"""
        dao.py: 数据库数据操作封装模块

        封装常用的增删改查操作

        提供事务支持

        实现单例模式，保证全局只有一个数据操作实例
"""

from sqlalchemy.exc import SQLAlchemyError
from db_manager import DBManager
from models import User, Role


class UserDao:
    __instance = None
    def __init__(self):
        if UserDao.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserDao.__instance = self
    @staticmethod
    def get_instance():
        if UserDao.__instance == None:
            UserDao()
        return UserDao.__instance
    def add_user(self, user):
        session = DBManager.get_instance().get_session()
        try:
            session.add(user)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            DBManager.get_instance().close_session()
    def delete_user(self, user):
        session = DBManager.get_instance().get_session()
        try:
            session.delete(user)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            DBManager.get_instance().close_session()
    def update_user(self, user):
        session = DBManager.get_instance().get_session()
        try:
            session.merge(user)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            DBManager.get_instance().close_session()
    def get_user_by_id(self, user_id):
        session = DBManager.get_instance().get_session()
        try:
            return session.query(User).filter(User.id == user_id).first()
        except SQLAlchemyError as e:
            raise e
        finally:
            DBManager.get_instance().close_session()
    def get_user_by_name(self, user_name):
        session = DBManager.get_instance().get_session()
        try:
            return session.query(User).filter(User.name == user_name).first()
        except SQLAlchemyError as e:
            raise e
        finally:
            DBManager.get_instance().close_session()
    def get_users_by_role(self, role_name):
        session = DBManager.get_instance().get_session()
        try:
            return session.query(User).join(User.role).filter(Role.name == role_name).all()
        except SQLAlchemyError as e:
            raise e
        finally:
            DBManager.get_instance().close_session()