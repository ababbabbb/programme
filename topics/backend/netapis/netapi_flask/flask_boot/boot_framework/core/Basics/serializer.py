from typing import Optional

from flask_sqlalchemy import SQLAlchemy


class BasicSerializer:
    db: Optional[SQLAlchemy] = None
    fields_excluded: Optional[list] = None
    model = None

    def __init__(self, instance=None, data=None, **kwargs):
        self.instance = instance
        self._initial_data = data
        self.errors = {}
        self.fields = self.get_fields()
        self.context = kwargs.get('context', {})

    def get_fields(self):
        return {}

    def is_valid(self):
        self.errors = {}
        for field_name, field in self.fields.items():
            value = self._initial_data.get(field_name)
            try:
                field.validate(value)
            except ValidationError as e:
                self.errors[field_name] = str(e)
        return not bool(self.errors)

    def save(self):
        if self.is_valid():
            if self.instance:
                self.update_instance()
            else:
                self.create_instance()

    def create_instance(self):
        model_class = self.get_model_class()
        instance = model_class(**self.data)
        self.db.session.add(instance)
        self.db.session.commit()

    def update_instance(self):
        for field_name, value in self._initial_data.items():
            setattr(self.instance, field_name, value)
        self.db.session.commit()

    def get_model_class(self):
        raise NotImplementedError("Must implement get_model_class() method")

    @property
    def data(self):
        return {
            key: value for key, value in self.instance.__dict__.items() if
            key not in self.fields_excluded and key in self.instance.__table__.columns
        }


class StringField:
    def __init__(self, required=False, max_length=None):
        self.required = required
        self.max_length = max_length

    def validate(self, value):
        if self.required and (value is None or value == ''):
            raise ValidationError("This field is required.")
        if self.max_length and len(value) > self.max_length:
            raise ValidationError("Max length exceeded.")


class IntegerField:
    def __init__(self, required=False, min_value=None, max_value=None):
        self.required = required
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if self.required and value is None:
            raise ValidationError("This field is required.")
        if self.min_value is not None and value < self.min_value:
            raise ValidationError("Value is too small.")
        if self.max_value is not None and value > self.max_value:
            raise ValidationError("Value is too large.")


class ValidationError(Exception):
    pass
