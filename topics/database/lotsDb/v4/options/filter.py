class Filter:
    def __init__(self, field, value):
        self._field = field
        self._value = value
    def __and__(self, other):
        return AndFilter(self, other)
    def __or__(self, other):
        return OrFilter(self, other)
    def __invert__(self):
        return NotFilter(self)
    def apply(self, data):
        raise NotImplementedError
class AndFilter(Filter):
    def __init__(self, left, right):
        super().__init__(None, None)
        self._left = left
        self._right = right
    def apply(self, data):
        left_data = self._left.apply(data)
        return self._right.apply(left_data)
class OrFilter(Filter):
    def __init__(self, left, right):
        super().__init__(None, None)
        self._left = left
        self._right = right
    def apply(self, data):
        left_data = self._left.apply(data)
        right_data = self._right.apply(data)
        return left_data.union(right_data)
class NotFilter(Filter):
    def __init__(self, filter_obj):
        super().__init__(None, None)
        self._filter_obj = filter_obj
    def apply(self, data):
        filter_data = self._filter_obj.apply(data)
        return data.difference(filter_data)
class EqualFilter(Filter):
    def apply(self, data):
        return {item for item in data if item[self._field] == self._value}
class NotEqualFilter(Filter):
    def apply(self, data):
        return {item for item in data if item[self._field] != self._value}
class GreaterThanFilter(Filter):
    def apply(self, data):
        return {item for item in data if item[self._field] > self._value}
class LessThanFilter(Filter):
    def apply(self, data):
        return {item for item in data if item[self._field] < self._value}
class ContainsFilter(Filter):
    def apply(self, data):
        return {item for item in data if self._value in item[self._field]}