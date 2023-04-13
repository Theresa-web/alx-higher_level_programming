#!/usr/bin/python3
def class_to_json(obj):
    # Get all attributes of the object
    attrs = vars(obj)

    # Create a dictionary to store the serialized data
    data = {}

    # Iterate over the attributes and serialize them
    for attr, value in attrs.items():
        # Check if the value is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value

    return data
