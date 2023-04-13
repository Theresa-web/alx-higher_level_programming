#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list from file, or create an empty list
try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

# Add command-line arguments to list
for arg in sys.argv[1:]:
    my_list.append(arg)

# Save list to file
save_to_json_file(my_list, filename)

# Print the updated list
print(my_list)
