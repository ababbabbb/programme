from connect import DBConnectionFactory
from model import Model, IntegerField, StringField


db_conn_factory = DBConnectionFactory()
mysql_conn = db_conn_factory.create_connection("mysql", "testdb", user="root", password="123456", host="localhost")

class User(Model):
    id = IntegerField("mysql", "testdb", "id")
    name = StringField("mysql", "testdb", "name")
    age = IntegerField("mysql", "testdb", "age")

User.create_table("mysql", "testdb", user="root", password="123456", host="localhost")


user = User(name="Tom", age=18)
user.save()

users = User.select("mysql", "testdb", fields=["name"], where="age>10", user="root", password="123456", host="localhost")
for user in users:
    print(user.name)

User.delete("mysql", "testdb", where="age<10", user="root", password="123456", host="localhost")

User.truncate("mysql", "testdb", user="root", password="123456", host="localhost")
