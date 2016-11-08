#!/usr/bin/env python3

my_list = [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33, 10]

my_bytes = bytes(my_list)

with open('file.txt', 'wb') as f:
    f.write(my_bytes)

my_str = my_bytes.decode('ascii')
print(repr(my_str))
