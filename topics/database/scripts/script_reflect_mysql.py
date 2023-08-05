from sqlalchemy import create_engine, inspect, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
import uuid

# 创建数据库引擎
engine = create_engine('mysql+pymysql://cabits_dev:hongpu8192@192.168.3.233:3306/cabits_dev')

# 获取数据库中所有表的结构
inspector = inspect(engine)
table_names = inspector.get_table_names()

# 遍历每个表的结构，并获取每个字段的类型、外键、名称、长度限制、默认值等条件设置
for table_name in table_names:
    table_columns = inspector.get_columns(table_name)
    table_fks = inspector.get_foreign_keys(table_name)
    model_name = table_name.capitalize()

    # 定义 SQLAlchemy 模型
    class_definition = f"class {model_name}(Base):\n    __tablename__ = '{table_name}'\n"
    has_primary_key = False
    for column in table_columns:
        column_name = column['name']
        column_type = column['type']
        column_nullable = column['nullable']
        column_default = column['default']
        column_primary_key = column.get('primary_key', False)
        column_is_fk = False

        # 判断当前字段是否为主键
        if column_primary_key:
            if column_type.python_type is uuid.UUID:
                column_kwargs = {
                    'primary_key': True,
                    'default': str(uuid.uuid4()),
                    'nullable': False,
                }
                has_primary_key = True
            else:
                column_kwargs = {
                    'primary_key': True,
                    'autoincrement': True,
                    'nullable': False,
                }
                has_primary_key = True
        # 如果当前字段不是主键，则根据字段类型、名称、长度限制、默认值等条件设置生成相应的 SQLAlchemy 模型定义
        else:
            column_kwargs = {
                'nullable': column_nullable,
            }
            if column_default is not None:
                column_kwargs['server_default'] = str(column_default)
            if isinstance(column_type, Integer):
                column_kwargs['autoincrement'] = column.get('autoincrement', False)
                column_kwargs['unsigned'] = column.get('unsigned', False)
                column_definition = f"    {column_name} = Column(Integer, **{column_kwargs})"
            elif isinstance(column_type, String):
                column_length = column_type.length
                column_kwargs['collation'] = column.get('collation', None)
                column_kwargs['server_onupdate'] = column.get('server_onupdate', None)
                default_value = column_default if column_default is not None else "''"
                column_definition = f"    {column_name} = Column(String({column_length}), server_default='{default_value}', **{column_kwargs})"
            elif isinstance(column_type, Float):
                column_kwargs['precision'] = column.get('precision', None)
                column_kwargs['scale'] = column.get('scale', None)
                column_kwargs['asdecimal'] = column.get('asdecimal', True)
                default_value = column_default if column_default is not None else "0.0"
                column_definition = f"    {column_name} = Column(Float, server_default='{default_value}', **{column_kwargs})"
            elif isinstance(column_type, Boolean):
                default_value = column_default if column_default is not None else "false"
                column_definition = f"    {column_name} = Column(Boolean, server_default='{default_value}', **{column_kwargs})"
            elif isinstance(column_type, DateTime):
                column_kwargs['timezone'] = column.get('timezone', False)
                default_value = column_default if column_default is not None else "CURRENT_TIMESTAMP"
                column_definition = f"    {column_name} = Column(DateTime, server_default='{default_value}', **{column_kwargs})"
            else:
                column_definition = f"    # {column_name} = Column({column_type}, **{column_kwargs})"
        class_definition += f"\n{column_definition}"

    # 如果该表没有设置主键，则自动添加一个整型自增主键或 UUID 主键
    if not has_primary_key:
        class_definition += f"\n    # id = Column(Integer, primary_key=True, autoincrement=True)"
        class_definition += f"\n    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))"

    # 获取表的备注信息
    table_comment = inspector.get_table_comment(table_name)
    if table_comment:
        class_definition += f"\n\n    __table_args__ = {{'comment': '{table_comment}'}}"

    # 获取表的索引信息
    table_indexes = inspector.get_indexes(table_name)
    for index in table_indexes:
        index_name = index['name']
        index_columns = index['column_names']
        index_is_unique = index['unique']
        index_definition = f"\n\n    {index_name} = Index('{index_name}', {' '.join(index_columns)}, unique={index_is_unique})"
        class_definition += index_definition

    # 打印生成的 SQLAlchemy 模型定义
    print(class_definition)
