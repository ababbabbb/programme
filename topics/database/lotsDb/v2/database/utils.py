

def create_table(conn, model):
    fields = []
    for field in model._meta.fields:
        if isinstance(field, models.AutoField):
            fields.append(f'{field.name} INT PRIMARY KEY AUTO_INCREMENT')
        elif isinstance(field, models.CharField):
            fields.append(f'{field.name} VARCHAR({field.max_length})')
        elif isinstance(field, models.IntegerField):
            fields.append(f'{field.name} INT')
        elif isinstance(field, models.EmailField):
            fields.append(f'{field.name} VARCHAR(254)')
        else:
            raise ValueError(f'Unsupported field type: {field.__class__.__name__}')
    create_sql = 'CREATE TABLE IF NOT EXISTS %s (%s)' % (model._meta.db_table, ', '.join(fields))
    conn.execute(create_sql)
