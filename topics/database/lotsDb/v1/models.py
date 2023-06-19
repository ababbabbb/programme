"""
        models.py: 数据库数据模型定义

        根据需要定义ORM模型类，用于映射数据库中的表或者文档

        使用SQLAlchemy提供的装饰器定义模型类中的字段和关系
"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'))

    role = relationship("Role", back_populates="users")


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)

    users = relationship("User", back_populates="role")