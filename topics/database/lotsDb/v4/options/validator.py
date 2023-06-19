class Validator:
    def validate(self, value):
        raise NotImplementedError
class NotEmptyValidator(Validator):
    def validate(self, value):
        if value == "":
            raise ValueError("Value cannot be empty")
class StringLengthValidator(Validator):
    def __init__(self, min_length=None, max_length=None):
        self._min_length = min_length
        self._max_length = max_length
    def validate(self, value):
        if self._min_length is not None and len(value) < self._min_length:
            raise ValueError(f"Value length must be at least {self._min_length}")
        if self._max_length is not None and len(value) > self._max_length:
            raise ValueError(f"Value length must be at most {self._max_length}")
class IntRangeValidator(Validator):
    def __init__(self, min_value=None, max_value=None):
        self._min_value = min_value
        self._max_value = max_value
    def validate(self, value):
        if self._min_value is not None and value < self._min_value:
            raise ValueError(f"Value must be at least {self._min_value}")
        if self._max_value is not None and value > self._max_value:
            raise ValueError(f"Value must be at most {self._max_value}")