import re

# 指定 Django 模型文件的路径
MODEL_FILE_PATH = "/home/bct/projects/cabits_dev_datasource/cabits/src/cabits/apps/facility/models.py"

# 定义 Django 模型中支持的字段类型和对应的 SQLAlchemy 字段类型
FIELD_TYPES_MAPPING = {
    'AutoField': 'BigInteger',
    'BigAutoField': 'BigInteger',
    'IntegerField': 'Integer',
    'BigIntegerField': 'BigInteger',
    'SmallIntegerField': 'Integer',
    'PositiveIntegerField': 'Integer',
    'PositiveSmallIntegerField': 'Integer',
    'CharField': 'String',
    'TextField': 'Text',
    'UUIDField': 'String',
    'ForeignKey': 'ForeignKey',
    'FloatField': 'Float',
    'BooleanField': 'Boolean',
    'DateTimeField': 'DateTime',
    'EnumField': 'Enum',
    'JSONField': 'JSON',
    'TimeField': 'Time',
    'DateField': 'Date'
}

# 读取 Django 模型文件
with open(MODEL_FILE_PATH, 'r') as f:
    model_file = f.read()

# 使用正则表达式匹配 Django 模型文件中的模型定义
model_definitions = re.findall(r'class\s+(\w+)\(.*?\):\s*\n(.*?)(?=class\s+\w+|$)', model_file, re.DOTALL)

# 遍历每个模型定义，并根据 Django 模型字段类型生成相应的 SQLAlchemy 模型定义
for model_name, model_definition in model_definitions:
    table_name = model_name.lower()

    class_definition = f"class {model_name}(Base):\n    __tablename__ = '{table_name}'\n"

    # 使用正则表达式匹配 Django 模型定义中的字段信息
    fields = re.findall(r'(\w+)\s*=\s*models\.(\w+)\((.*?)\)', model_definition, re.DOTALL)
    for field in fields:
        field_name = field[0]
        field_type = FIELD_TYPES_MAPPING.get(field[1])
        field_options = field[2]

        column_kwargs = {'nullable': 'False'}
        column_definition = None

        # 根据 Django 模型字段类型生成相应的 SQLAlchemy 模型定义
        if field_type == 'Integer':
            column_definition = f"    {field_name} = Column(Integer, **{column_kwargs})"
        elif field_type == 'String':
            max_length = re.findall(r'max_length=(\d+)', field_options)
            if max_length:
                max_length = int(max_length[0])
                column_definition = f"    {field_name} = Column(String({max_length}), **{column_kwargs})"
        elif field_type == 'ForeignKey':
            to_field = re.findall(r'to=[\'|"](\w+)[\'|"]', field_options)
            if to_field:
                to_field = to_field[0]
                column_definition = f"    {field_name}_id = Column(Integer, ForeignKey('{to_field}.id'), **{column_kwargs})"
                column_kwargs = {'nullable': 'True'}
        elif field_type == 'Float':
            column_definition = f"    {field_name} = Column(Float, **{column_kwargs})"
        elif field_type == 'Boolean':
            column_definition = f"    {field_name} = Column(Boolean, **{column_kwargs})"
        elif field_type == 'DateTime':
            column_definition = f"    {field_name} = Column(DateTime, **{column_kwargs})"
        elif field_type == 'Enum':
            choices = re.findall(r'choices=\[(.*?)\]', field_options, re.DOTALL)
            if choices:
                choices = [c.strip().replace("'", '') for c in choices[0].split(',')]
                column_definition = f"    {field_name} = Column(Enum(*{choices}), **{column_kwargs})"
        elif field_type == 'JSON':
            column_definition = f"    {field_name} = Column(JSON, **{column_kwargs})"
        elif field_type == 'Text':
            column_definition = f"    {field_name} = Column(Text, **{column_kwargs})"
        elif field_type == 'Time':
            column_definition = f"    {field_name} = Column(Time, **{column_kwargs})"
        elif field_type == 'Date':
            column_definition = f"    {field_name} = Column(Date, **{column_kwargs})"
        elif field_type == 'BigInteger':
            column_definition = f"    {field_name} = Column(BigInteger, **{column_kwargs})"
            # 将生成的 SQLAlchemy 字段定义添加到模型定义中
        if column_definition:
            class_definition += f"{column_definition}\n"

    # 在控制台中打印出生成的 SQLAlchemy 模型定义
    print('')
    print(class_definition)
