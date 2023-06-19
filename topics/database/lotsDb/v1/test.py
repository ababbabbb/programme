from dao import UserDao
from models import User, Role
from db_manager import DBManager


# 初始化数据库连接
DBManager.get_instance().init_engine('mysql', 'localhost', '3306', 'root', '123456', 'test')
# 添加用户
user_dao = UserDao.get_instance()
role = Role(name='admin')
user = User(name='admin', email='admin@gmail.com', password='123456', role=role)
user_dao.add_user(user)
# 获取用户
user = user_dao.get_user_by_name('admin')
print(user.name, user.email, user.role.name)
# 获取角色下的所有用户
users = user_dao.get_users_by_role('admin')
for user in users:
    print(user.name, user.email, user.role.name)