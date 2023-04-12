#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, mode="r", encoding="utf8") as f:
            print(f.read())
    except:
        pass
