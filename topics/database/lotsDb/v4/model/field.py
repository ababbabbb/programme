class Field:
    def __init__(self, db_type, db_name, field_name, field_type, validators=None):
        self._db_type = db_type
        self._db_name = db_name
        self._field_name = field_name
        self._field_type = field_type
        self._validators = validators or []
    def validate(self, value):
        for validator in self._validators:
            validator.validate(value)
    def to_sql(self):
        raise NotImplementedError
class StringField(Field):
    def to_sql(self):
        return f"{self._field_name} VARCHAR(255)"
class IntegerField(Field):
    def to_sql(self):
        return f"{self._field_name} INT"