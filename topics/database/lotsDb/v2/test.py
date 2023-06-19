from database import get_connection, create_table
from database.models import Person


# 连接MySQL数据库
conn = get_connection('mysql', host='localhost', user='root', password='123456', database='test')
# 创建表格
create_table(conn, Person)
# 插入数据
person = Person(name='Alice', age=20, email='alice@example.com')
person.save()
# 查询数据
persons = Person.objects.filter(age__gte=18)
for p in persons:
    print(p.name, p.age, p.email)
# 关闭连接
conn.close()