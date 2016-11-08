#!/usr/bin/env python2

my_list = [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33, 10]

my_str = ''.join(chr(i) for i in my_list)

with open('file.txt', 'w') as f:
    f.write(my_str)

my_ustr = my_str.decode('ascii')
print(repr(my_ustr))
