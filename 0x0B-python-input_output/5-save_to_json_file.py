#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(my_obj, file, ensure_ascii=False)
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")
