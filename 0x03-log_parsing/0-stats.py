#!/usr/bin/python3
import sys

codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        split_line = line.split()
        try:
            status_code = split_line[-2]
            file_size = int(split_line[-1])
            if status_code in codes:
                codes[status_code] += 1
            total_size += file_size
        except Exception:
            pass
        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for k in sorted(codes.keys()):
                if codes[k] != 0:
                    print("{}: {}".format(k, codes[k]))
finally:
    print("File size: {}".format(total_size))
    for k in sorted(codes.keys()):
        if codes[k] != 0:
            print("{}: {}".format(k, codes[k]))
