#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        # Create a dictionary to store the serialized data
        data = {}

        # Serialize the instance attributes
        data['first_name'] = self.first_name
        data['last_name'] = self.last_name
        data['age'] = self.age

        return data
