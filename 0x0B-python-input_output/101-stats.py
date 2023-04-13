#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) > 2:
                size = int(tokens[-1])
                status = tokens[-2]
                total_size += size
                if status in status_codes:
                    status_codes[status] += 1
            count += 1
            if count == 10:
                print("File size: {}".format(total_size))
                for key in sorted(status_codes.keys()):
                    if status_codes[key] > 0:
                        print("{}: {}".format(key, status_codes[key]))
                count = 0
        print("File size: {}".format(total_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key] > 0:
                print("{}: {}".format(key, status_codes[key]))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key] > 0:
                print("{}: {}".format(key, status_codes[key]))
        sys.exit(0)
