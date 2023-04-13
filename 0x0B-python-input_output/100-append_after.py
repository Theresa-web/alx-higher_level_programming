#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    # Open the file for reading and writing
    with open(filename, "r+") as f:
        # Read the contents of the file into a list of lines
        lines = f.readlines()

        # Loop over the lines in the file
        for i, line in enumerate(lines):
            # Check if the search string is in the line
            if search_string in line:
                # Insert the new string after the current line
                lines.insert(i+1, new_string + "\n")

        # Write the modified lines back to the file
        f.seek(0)
        f.writelines(lines)
