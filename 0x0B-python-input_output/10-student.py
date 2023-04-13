#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        # If no attributes are specified, serialize all attributes
        if attrs is None:
            return self.__dict__

        # Serialize only the specified attributes
        data = {}
        for attr in attrs:
            if hasattr(self, attr):
                data[attr] = getattr(self, attr)
        return data
