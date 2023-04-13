def write_file(filename="", text=""):
    # Open file for writing using with statement
    with open(filename, 'w', encoding='utf8') as f:
        # Write text to file and get the number of characters written
        num_chars = f.write(text)
    
    # Return the number of characters written
    return num_chars
